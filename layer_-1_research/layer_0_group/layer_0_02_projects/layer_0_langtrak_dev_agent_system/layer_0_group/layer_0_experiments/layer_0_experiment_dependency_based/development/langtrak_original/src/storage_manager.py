#!/usr/bin/env python3
# resource_id: "d0bbbdcd-77fc-4599-a8b6-6b5432215067"
# resource_type: "document"
# resource_name: "storage_manager"
"""
Storage Manager - Hybrid Local/Cloud Data Management
Handles both SQLite (local) and Firestore (cloud) storage with migration capabilities
"""
import sqlite3
import os
import json
from datetime import datetime, timezone
from collections import defaultdict
from enum import Enum
from services.firebase import clean_firebase_service, firestore_db
import main

SQLITE_TIMEOUT = 20.0

class StorageType(Enum):
    LOCAL = "local"
    CLOUD = "cloud"
    HYBRID = "hybrid"

class StorageManager:
    def __init__(self):
        self.default_storage = StorageType.CLOUD  # Firebase default
        self._words_columns = None
        self._phoneme_columns = None
        self._project_columns = None
        # Lazy initialization: do NOT call _ensure_column_cache() here
        # It causes import-time side effects (DB connection) that break tests

    def _connect(self):
        # Ensure database directory exists before connecting
        db_path = main.DB_NAME
        db_dir = os.path.dirname(db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
            
        conn = sqlite3.connect(db_path, timeout=SQLITE_TIMEOUT, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;") # Ensure foreign keys are enabled
        return conn

    def _get_user_firebase_uid(self, user_id):
        if user_id is None:
            return None
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT firebase_uid FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            return row[0] if row and row[0] else None
        finally:
            conn.close()

    # --- metadata helpers ---
    def _variant_key(self, storage_type, identifier):
        if identifier is None:
            return None
        return f"{storage_type}:{identifier}"

    def _ensure_group_metadata(self, group_identifier_str, default_name, user_id, parent_group_id=None):
        print(f"DEBUG SM: _ensure_group_metadata called with group_identifier_str={group_identifier_str}, user_id={user_id}")
        if not group_identifier_str:
            return {'group_id': None, 'name': default_name, 'parent_group_id': parent_group_id} # This group_id would refer to the internal INTEGER ID

        conn = self._connect()
        try:
            cursor = conn.cursor()

            # Ensure user exists in this connection's context before attempting FK inserts
            cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
            user_check = cursor.fetchone()
            if not user_check:
                print(f"CRITICAL ERROR SM: User {user_id} NOT FOUND in _ensure_group_metadata's connection ({id(conn)}) before group_memberships insert.")
                raise Exception(f"User {user_id} not found in connection for group operations, FK constraint will fail.")
            else:
                print(f"DEBUG SM: User {user_id} found in _ensure_group_metadata's connection ({id(conn)}).")

            # First, try to find an existing group by its string identifier
            cursor.execute("""
                SELECT id, name, parent_group_id FROM project_groups
                WHERE group_identifier = ? AND user_id = ?
            """, (group_identifier_str, user_id))
            row = cursor.fetchone()

            group_internal_id = None # This will be the INTEGER ID from the DB
            name = default_name or 'Untitled Project'
            existing_parent = parent_group_id

            if row: # Group found by identifier
                group_internal_id = row[0]
                name = row[1] or default_name
                existing_parent = row[2]
                print(f"DEBUG SM: _ensure_group_metadata found existing group_internal_id={group_internal_id} for {group_identifier_str}")

                # Update if parent_group_id has changed
                if parent_group_id is not None and existing_parent != parent_group_id:
                    cursor.execute("""
                        UPDATE project_groups
                        SET parent_group_id = ?, updated_at = CURRENT_TIMESTAMP
                        WHERE id = ? AND user_id = ?
                    """, (parent_group_id, group_internal_id, user_id))
                    conn.commit()
                    print(f"DEBUG SM: _ensure_group_metadata updated parent_group_id for {group_identifier_str}")

            else: # Group not found by identifier, create a new one
                cursor.execute("""
                    INSERT INTO project_groups (group_identifier, user_id, name, parent_group_id)
                    VALUES (?, ?, ?, ?)
                """, (group_identifier_str, user_id, default_name or 'Untitled Project', parent_group_id))
                group_internal_id = cursor.lastrowid
                conn.commit() # Commit after insert to get lastrowid
                print(f"DEBUG SM: _ensure_group_metadata created new group_internal_id={group_internal_id} for {group_identifier_str}")
            
            # Add PRAGMA foreign_keys = ON; just before the insert to be absolutely sure.
            # Debugging schema before FK insert
            cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='users'")
            print(f"DEBUG SM: users schema: {cursor.fetchone()}")
            cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='project_groups'")
            print(f"DEBUG SM: project_groups schema: {cursor.fetchone()}")
            cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='group_memberships'")
            print(f"DEBUG SM: group_memberships schema: {cursor.fetchone()}")

            # Add PRAGMA foreign_keys = ON; just before the insert to be absolutely sure.
            cursor.execute("PRAGMA foreign_keys = ON;")
            print(f"DEBUG SM: Attempting INSERT OR IGNORE into group_memberships with group_id={group_internal_id}, user_id={user_id}")
            # Ensure the user who initiated the creation/retrieval of this group is a member
            cursor.execute("""
                INSERT OR IGNORE INTO group_memberships (group_id, user_id)
                VALUES (?, ?)
            """, (group_internal_id, user_id))
            conn.commit()
            print(f"DEBUG SM: _ensure_group_metadata ensured user {user_id} is member of group {group_internal_id}")


            # After insert or update, retrieve the latest metadata
            cursor.execute("""
                SELECT id, name, parent_group_id FROM project_groups
                WHERE group_identifier = ? AND user_id = ?
            """, (group_identifier_str, user_id)) # Query again, in case of race condition or update
            final_row = cursor.fetchone()

            if final_row:
                result = {
                    'group_id': final_row[0], # Return the internal INTEGER ID
                    'group_identifier': group_identifier_str, # Also return the string identifier
                    'name': final_row[1],
                    'parent_group_id': final_row[2]
                }
                print(f"DEBUG SM: _ensure_group_metadata returning: {result}")
                return result
            else:
                # Should not happen if INSERT or SELECT works correctly
                raise Exception(f"Failed to retrieve group metadata for {group_identifier_str}")

        finally:
            conn.close()

    def _get_group_metadata(self, group_identifier_str, user_id):
        print(f"DEBUG SM: _get_group_metadata called for group_identifier_str={group_identifier_str}, user_id={user_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, parent_group_id FROM project_groups
                WHERE group_identifier = ? AND user_id = ?
            """, (group_identifier_str, user_id))
            row = cursor.fetchone()
            if row:
                result = {'group_id': row[0], 'group_identifier': group_identifier_str, 'name': row[1], 'parent_group_id': row[2]}
                print(f"DEBUG SM: _get_group_metadata found: {result}")
                return result
            print(f"DEBUG SM: _get_group_metadata found no match for {group_identifier_str}")
            return None
        finally:
            conn.close()

    def _ensure_variant_metadata(self, variant_identifier, group_internal_id, storage_type, user_id, default_branch_name=None, parent_identifier=None):
        print(f"DEBUG SM: _ensure_variant_metadata called with variant_identifier={variant_identifier}, group_internal_id={group_internal_id}, user_id={user_id}")
        if not variant_identifier or user_id is None:
            return {
                'variant_identifier': variant_identifier,
                'group_id': group_internal_id,
                'branch_name': default_branch_name,
                'parent_variant_identifier': parent_identifier
            }

        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT group_id, parent_variant_identifier, branch_name
                FROM project_variants_meta
                WHERE variant_identifier = ? AND user_id = ?
            """, (variant_identifier, user_id))
            row = cursor.fetchone()
            if row:
                current_group_internal_id, parent_id, branch_name = row
                if current_group_internal_id != group_internal_id and group_internal_id is not None:
                    cursor.execute("""
                        UPDATE project_variants_meta
                        SET group_id = ?, updated_at = CURRENT_TIMESTAMP
                        WHERE variant_identifier = ? AND user_id = ?
                    """, (group_internal_id, variant_identifier, user_id))
                    conn.commit()
                    current_group_internal_id = group_internal_id
                    print(f"DEBUG SM: _ensure_variant_metadata updated group_id for {variant_identifier}")
                result = {
                    'variant_identifier': variant_identifier,
                    'group_id': current_group_internal_id,
                    'parent_variant_identifier': parent_id,
                    'branch_name': branch_name
                }
                print(f"DEBUG SM: _ensure_variant_metadata found existing variant metadata: {result}")
                return result

            cursor.execute("""
                INSERT INTO project_variants_meta (
                    variant_identifier, group_id, user_id, storage_type,
                    parent_variant_identifier, branch_name
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                variant_identifier,
                group_internal_id, # This is now ensured to be an INTEGER
                user_id,
                storage_type,
                parent_identifier,
                default_branch_name
            ))
            conn.commit()
            result = {
                'variant_identifier': variant_identifier,
                'group_id': group_internal_id,
                'parent_variant_identifier': parent_identifier,
                'branch_name': default_branch_name
            }
            print(f"DEBUG SM: _ensure_variant_metadata created new variant metadata: {result}")
            return result
        finally:
            conn.close()

    def _get_variant_metadata(self, variant_identifier, user_id):
        print(f"DEBUG SM: _get_variant_metadata called for variant_identifier={variant_identifier}, user_id={user_id}")
        if not variant_identifier:
            return None
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT group_id, storage_type, parent_variant_identifier, branch_name
                FROM project_variants_meta
                WHERE variant_identifier = ? AND user_id = ?
            """, (variant_identifier, user_id))
            row = cursor.fetchone()
            if row:
                result = {
                    'variant_identifier': variant_identifier,
                    'group_id': row[0],
                    'storage_type': row[1],
                    'parent_variant_identifier': row[2],
                    'branch_name': row[3]
                }
                print(f"DEBUG SM: _get_variant_metadata found: {result}")
                return result
            print(f"DEBUG SM: _get_variant_metadata found no match for {variant_identifier}")
            return None
        finally:
            conn.close()

    def _fetch_project_metadata(self, storage_type, identifier, owner_id=None):
        owner_str = str(owner_id) if owner_id is not None else None
        print(f"DEBUG SM: _fetch_project_metadata called for storage_type={storage_type}, identifier={identifier}, owner_id={owner_id}")

        if storage_type == 'local':
            try:
                int_id = int(identifier)
            except (TypeError, ValueError):
                print(f"DEBUG SM: _fetch_project_metadata invalid local identifier: {identifier}")
                return None

            conn = self._connect()
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, name, user_id, cloud_project_id, updated_at
                    FROM projects
                    WHERE id = ?
                """, (int_id,))
                row = cursor.fetchone()
            finally:
                conn.close()

            if not row:
                print(f"DEBUG SM: _fetch_project_metadata no local project found for id: {int_id}")
                return None

            if owner_str is not None and str(row[2]) != owner_str:
                print(f"DEBUG SM: _fetch_project_metadata access denied for local project {int_id}, owner mismatch {row[2]} != {owner_str}")
                return None

            result = {
                'storage_type': 'local',
                'project_id': str(row[0]),
                'cloud_project_id': row[3],
                'name': row[1],
                'owner_user_id': row[2],
                'updated_at': row[4]
            }
            print(f"DEBUG SM: _fetch_project_metadata returning local project: {result}")
            return result

        if not clean_firebase_service.is_available():
            print("DEBUG SM: _fetch_project_metadata cloud storage not available")
            return None

        try:
            project_doc = firestore_db.get_project(identifier)
        except Exception as exc:
            print(f"DEBUG SM: _fetch_project_metadata Error fetching cloud project {identifier}: {exc}")
            project_doc = None

        if not project_doc:
            print(f"DEBUG SM: _fetch_project_metadata no cloud project found for id: {identifier}")
            return None

        doc_owner = project_doc.get('user_id')
        if doc_owner is None:
            doc_owner = project_doc.get('user_id_str')

        if doc_owner is not None and isinstance(doc_owner, (int, float)):
            doc_owner = str(int(doc_owner))
        elif doc_owner is not None:
            doc_owner = str(doc_owner)

        if owner_str is not None and doc_owner is not None and doc_owner != owner_str:
            print(f"DEBUG SM: _fetch_project_metadata access denied for cloud project {identifier}, owner mismatch {doc_owner} != {owner_str}")
            return None

        result = {
            'storage_type': 'cloud',
            'project_id': None,
            'cloud_project_id': identifier,
            'name': project_doc.get('name', 'Cloud Project'),
            'owner_user_id': doc_owner,
            'updated_at': project_doc.get('updated_at')
        }
        print(f"DEBUG SM: _fetch_project_metadata returning cloud project: {result}")
        return result
        
    def get_storage_preference(self, user_id=None, project_id=None):
        """Get storage preference for user or project"""
        print(f"DEBUG SM: get_storage_preference called for user_id={user_id}, project_id={project_id}")
        # For now, check if Firebase is available
        if clean_firebase_service.is_available():
            print("DEBUG SM: get_storage_preference returning CLOUD")
            return StorageType.CLOUD
        else:
            print("DEBUG SM: get_storage_preference returning LOCAL")
            return StorageType.LOCAL
    
    def get_project_storage_type(self, project_id):
        """Get the storage type for a specific project"""
        print(f"DEBUG SM: get_project_storage_type called for project_id={project_id}")
        # First check if project exists in cloud storage
        if clean_firebase_service.is_available():
            try:
                cloud_project = firestore_db.get_project(project_id)
                if cloud_project:
                    print(f"DEBUG SM: get_project_storage_type cloud project {project_id} found")
                    return 'cloud'
            except Exception as e:
                print(f"DEBUG SM: get_project_storage_type Error checking cloud storage for project {project_id}: {e}")
        
        # Check if project exists in local storage
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM projects WHERE id = ?", (project_id,))
            local_project = cursor.fetchone()
            conn.close()
            
            if local_project:
                print(f"DEBUG SM: get_project_storage_type local project {project_id} found")
                return 'local'
        except Exception as e:
            print(f"DEBUG SM: get_project_storage_type Error checking local storage for project {project_id}: {e}")
        
        # Default to local if uncertain
        print(f"DEBUG SM: get_project_storage_type returning default local for {project_id}")
        return 'local'
    
    def create_project_with_storage(self, project_data, storage_type=None):
        """Create project with specified storage type"""
        print(f"DEBUG SM: create_project_with_storage called with project_data={project_data}, storage_type={storage_type}")
        if storage_type is None:
            storage_type = self.default_storage
            
        project_data['storage_type'] = storage_type.value
        project_data['created_at'] = datetime.utcnow()
        project_data['updated_at'] = datetime.utcnow()
        if not project_data.get('firebase_uid'):
            project_data['firebase_uid'] = self._get_user_firebase_uid(project_data.get('user_id'))
        
        if storage_type == StorageType.CLOUD and clean_firebase_service.is_available():
            # Create in Firestore
            print("DEBUG SM: create_project_with_storage creating cloud project")
            return firestore_db.create_project(project_data)
        else:
            # Create in SQLite
            print("DEBUG SM: create_project_with_storage creating local project")
            return self._create_project_sqlite(project_data)
    
    def _create_project_sqlite(self, project_data):
        """Create project in SQLite database"""
        print(f"DEBUG SM: _create_project_sqlite called with project_data={project_data}")
        conn = self._connect()
        try:
            cursor = conn.cursor()

            created_at = project_data.get('created_at')
            if not created_at:
                created_at = datetime.utcnow()
                project_data['created_at'] = created_at
            updated_at = project_data.get('updated_at') or created_at
            project_data['updated_at'] = updated_at
            cloud_last_sync = project_data.get('cloud_last_sync')
            if cloud_last_sync and hasattr(cloud_last_sync, 'isoformat'):
                cloud_last_sync = cloud_last_sync
            elif cloud_last_sync:
                pass

            cursor.execute("""
                INSERT INTO projects (name, user_id, created_at, updated_at, cloud_project_id, cloud_last_sync, migrated_to_cloud)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                project_data['name'],
                project_data['user_id'], 
                project_data['created_at'].isoformat(),
                project_data['updated_at'].isoformat(),
                project_data.get('cloud_project_id'),
                cloud_last_sync.isoformat() if isinstance(cloud_last_sync, datetime) else cloud_last_sync,
                1 if project_data.get('migrated_to_cloud') else 0
            ))

            project_id = cursor.lastrowid
            if project_id is None:
                raise Exception("Failed to retrieve project_id after insert")
            conn.commit()
            print(f"DEBUG SM: _create_project_sqlite successfully created project with id={project_id}")
            return project_id
        finally:
            conn.close()
    
    def get_projects(self, user_id, storage_type=None):
        """Get projects from specified storage, grouping local/cloud variants together."""
        print(f"DEBUG SM: get_projects called for user_id={user_id}, storage_type={storage_type}")
        cloud_available = clean_firebase_service.is_available()

        variant_nodes = {}
        parent = {}

        def node_id(kind, identifier):
            return f"{kind}:{identifier}"

        def make_node(node):
            if node not in parent:
                parent[node] = node

        def find(node):
            make_node(node)
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        type_order = {'local': 0, 'cloud': 1, 'cloud_placeholder': 2, 'local_placeholder': 3}

        def ensure_cloud_placeholder(cloud_id):
            node = node_id('cloud', cloud_id)
            if node not in variant_nodes:
                variant_nodes[node] = {
                    'variant_id': node,
                    'id': str(cloud_id),
                    'type': 'cloud_placeholder',
                    'name': f'Cloud Variant ({cloud_id})',
                    'display_label': 'Cloud (missing)',
                    'icon': '☁️',
                    'word_count': 0,
                    'created_at': '',
                    'updated_at': '',
                    'updated_display': None,
                    'cloud_project_id': str(cloud_id),
                    'cloud_last_sync': '',
                    'cloud_last_sync_display': None,
                    'placeholder': True,
                    'is_owner': True,
                    'recent_dt': None
                }
            return node

        def ensure_local_placeholder(local_id):
            node = node_id('local', local_id)
            if node not in variant_nodes:
                variant_nodes[node] = {
                    'variant_id': node,
                    'id': str(local_id),
                    'type': 'local_placeholder',
                    'name': f'Local Variant ({local_id})',
                    'display_label': 'Local (missing)',
                    'icon': '💾',
                    'word_count': 0,
                    'created_at': '',
                    'updated_at': '',
                    'updated_display': None,
                    'cloud_project_id': None,
                    'cloud_last_sync': '',
                    'cloud_last_sync_display': None,
                    'placeholder': True,
                    'is_owner': True,
                    'recent_dt': None
                }
            return node

        # Local variants
        if storage_type is None or storage_type == StorageType.LOCAL:
            try:
                for project in self._get_projects_sqlite(user_id):
                    local_id = str(project['id'])
                    node = node_id('local', local_id)
                    make_node(node)

                    created_iso = self._to_iso(project['created_at'])
                    updated_iso = self._to_iso(project['updated_at'])
                    cloud_last_iso = self._to_iso(project.get('cloud_last_sync'))
                    recent_dt = (self._parse_datetime(updated_iso) or
                                 self._parse_datetime(cloud_last_iso) or
                                 self._parse_datetime(created_iso))

                    variant_nodes[node] = {
                        'variant_id': node,
                        'id': local_id,
                        'type': 'local',
                        'name': project['name'],
                        'display_label': 'Local',
                        'icon': '💾',
                        'word_count': project.get('word_count', 0),
                        'created_at': created_iso,
                        'updated_at': updated_iso,
                        'updated_display': self._format_display(updated_iso),
                        'cloud_project_id': str(project['cloud_project_id']) if project.get('cloud_project_id') else None,
                        'cloud_last_sync': cloud_last_iso,
                        'cloud_last_sync_display': self._format_display(cloud_last_iso),
                        'placeholder': False,
                        'is_owner': True,
                        'recent_dt': recent_dt,
                        'variant_identifier': node
                    }
                    print(f"DEBUG SM: get_projects added local variant node: {variant_nodes[node]}")

                    if project.get('cloud_project_id'):
                        cloud_node = ensure_cloud_placeholder(project['cloud_project_id'])
                        union(node, cloud_node)
            except Exception as e:
                print(f"DEBUG SM: get_projects Error getting local projects: {e}")

        # Cloud variants
        if (storage_type is None or storage_type == StorageType.CLOUD) and cloud_available:
            try:
                cloud_projects = firestore_db.get_user_projects(user_id)
            except Exception as e:
                print(f"DEBUG SM: get_projects Error getting cloud projects: {e}")
                cloud_projects = []
        else:
            cloud_projects = []

        for project in cloud_projects:
            cloud_id = str(project.get('id'))
            node = node_id('cloud', cloud_id)
            make_node(node)

            created_iso = self._to_iso(project.get('created_at'))
            updated_iso = self._to_iso(project.get('updated_at'))
            recent_dt = (self._parse_datetime(updated_iso) or
                         self._parse_datetime(created_iso))

            variant_nodes[node] = {
                'variant_id': node,
                'id': cloud_id,
                'type': 'cloud',
                'name': project.get('name', 'Cloud Project'),
                'display_label': 'Cloud',
                'icon': '☁️',
                'word_count': firestore_db.count_project_words(project.get('id')),
                'created_at': created_iso,
                'updated_at': updated_iso,
                'updated_display': self._format_display(updated_iso),
                'cloud_project_id': cloud_id,
                'cloud_last_sync': updated_iso,
                'cloud_last_sync_display': self._format_display(updated_iso),
                'placeholder': False,
                'is_owner': True,
                'recent_dt': recent_dt,
                'variant_identifier': node,
                'original_sqlite_id': str(project.get('original_sqlite_id')) if project.get('original_sqlite_id') else None
            }
            print(f"DEBUG SM: get_projects added cloud variant node: {variant_nodes[node]}")

            if project.get('original_sqlite_id'):
                local_node = ensure_local_placeholder(project['original_sqlite_id'])
                union(node, local_node)

        # Build groups enriched with metadata
        group_map = defaultdict(list)
        group_roots = {} # Maps internal group_id (int) to root_identifier (str)

        for node_str, variant in variant_nodes.items():
            root_identifier = find(node_str) # This is a string like "local:1"

            # Ensure group metadata first to get the INTEGER group_id
            group_meta_for_root = self._ensure_group_metadata(root_identifier, variant.get('name'), user_id)
            group_internal_id = group_meta_for_root['group_id'] # This is the INTEGER ID
            print(f"DEBUG SM: get_projects processing variant {node_str}, root_identifier={root_identifier}, group_internal_id={group_internal_id}")

            if variant.get('placeholder'):
                # For placeholders, group_id can be the root_identifier string for grouping purposes
                # but we need the internal integer ID for FKs.
                variant['group_id'] = group_internal_id # Assign integer ID for internal use
            else:
                meta = self._ensure_variant_metadata(
                    variant.get('variant_identifier') or node_str, # variant_identifier is a string
                    group_internal_id, # Pass the INTEGER group_id here
                    variant.get('type'),
                    user_id,
                    default_branch_name='main'
                )
                variant['group_id'] = meta.get('group_id') or group_internal_id # This should now consistently be the INTEGER ID
                variant['branch_name'] = meta.get('branch_name')
                variant['parent_variant_identifier'] = meta.get('parent_variant_identifier')
            
            if not variant.get('group_id'): # Fallback for any case where group_id is not set
                variant['group_id'] = group_internal_id
            
            group_map[group_internal_id].append(variant) # Group by INTEGER ID
            group_roots[group_internal_id] = root_identifier # Keep root identifier for display if needed

        groups = []
        for group_internal_id, variants in group_map.items(): # Iterate by INTEGER group_id
            def variant_sort_key(v):
                dt = v.get('recent_dt') or self._parse_datetime(v.get('updated_at')) or datetime.min.replace(tzinfo=timezone.utc)
                return (type_order.get(v['type'], 99), -(dt.timestamp()))

            variants.sort(key=variant_sort_key)

            non_placeholder_cloud = [v for v in variants if v['type'] == 'cloud' and not v['placeholder']]
            non_placeholder_local = [v for v in variants if v['type'] == 'local' and not v['placeholder']]

            preferred_variant = None
            if non_placeholder_cloud:
                preferred_variant = non_placeholder_cloud[0]
                default_name = preferred_variant['name']
            elif non_placeholder_local:
                preferred_variant = non_placeholder_local[0]
                default_name = preferred_variant['name']
            else:
                preferred_variant = variants[0]
                default_name = preferred_variant['name']

            recent_dt = None
            for v in variants:
                if v.get('recent_dt'):
                    recent_dt = v['recent_dt'] if recent_dt is None else max(recent_dt, v['recent_dt'])

            owner_variant = non_placeholder_local[0] if non_placeholder_local else non_placeholder_cloud[0] if non_placeholder_cloud else variants[0]
            
            # Call _ensure_group_metadata with the string identifier to retrieve up-to-date group info
            group_meta = self._ensure_group_metadata(group_roots.get(group_internal_id), default_name, user_id)

            group = {
                'group_id': group_meta['group_id'], # Ensure this is the INTEGER ID
                'group_identifier': group_meta['group_identifier'], # Add string identifier for external use
                'name': group_meta['name'],
                'parent_group_id': group_meta.get('parent_group_id'),
                'variants': variants,
                'has_local': any(v['type'] == 'local' for v in variants),
                'has_cloud': any(v['type'] == 'cloud' for v in variants),
                'recent_dt': recent_dt,
                'recent_display': self._format_display(recent_dt),
                'owner_variant': owner_variant,
                'root_identifier': group_roots.get(group_internal_id),
                'preferred_variant_identifier': preferred_variant.get('variant_identifier') if preferred_variant else None,
                'preferred_variant_name': preferred_variant.get('name') if preferred_variant else None,
                'preferred_variant_placeholder': bool(preferred_variant.get('placeholder')) if preferred_variant else False,
                'preferred_variant_id': preferred_variant.get('id') if preferred_variant else None,
                'preferred_variant_type': preferred_variant.get('type') if preferred_variant else None
            }
            print(f"DEBUG SM: get_projects created group: {group}")

            group['local_variants'] = [v for v in variants if v['type'] == 'local']
            group['cloud_variants'] = [v for v in variants if v['type'] == 'cloud']

            local_count = len(group['local_variants'])
            cloud_count = len(group['cloud_variants'])
            summary_parts = []
            if local_count:
                summary_parts.append(f"Local x{local_count}")
            if cloud_count:
                summary_parts.append(f"Cloud x{cloud_count}")
            group['variant_summary'] = ' • '.join(summary_parts) if summary_parts else 'No variants yet'

            groups.append(group)

        group_dict = {g['group_id']: g for g in groups}
        for g in groups:
            g['subprojects'] = []

        for g in groups:
            parent_id = g.get('parent_group_id')
            if parent_id and parent_id in group_dict:
                group_dict[parent_id]['subprojects'].append(g)

        for g in groups:
            g['subprojects'].sort(key=lambda sg: (sg['name'].lower()))

        def group_sort_key(g):
            if g['recent_dt']:
                return (0, -g['recent_dt'].timestamp())
            return (1, g['name'].lower())

        roots = [g for g in groups if not g.get('parent_group_id')]
        roots.sort(key=group_sort_key)
        print(f"DEBUG SM: get_projects returning {len(roots)} root groups")
        return roots
    
    def _get_projects_sqlite(self, user_id):
        """Get projects from SQLite"""
        print(f"DEBUG SM: _get_projects_sqlite called for user_id={user_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, user_id, created_at, updated_at, cloud_project_id, cloud_last_sync, migrated_to_cloud
                FROM projects WHERE user_id = ?
                ORDER BY updated_at DESC
            """, (user_id,))

            projects = []
            rows = cursor.fetchall()
            for row in rows:
                cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (row[0],))
                word_count = cursor.fetchone()[0]
                project_data = {
                    'id': row[0],
                    'name': row[1],
                    'user_id': row[2],
                    'created_at': row[3],
                    'updated_at': row[4],
                    'cloud_project_id': row[5],
                    'cloud_last_sync': row[6],
                    'migrated_to_cloud': row[7],
                    'word_count': word_count
                }
                projects.append(project_data)
                print(f"DEBUG SM: _get_projects_sqlite fetched project: {project_data}")
            return projects
        finally:
            conn.close()

    def _get_project_sqlite_by_id(self, project_id):
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, user_id, created_at, updated_at, cloud_project_id, cloud_last_sync, migrated_to_cloud
                FROM projects WHERE id = ?
            """, (project_id,))
            row = cursor.fetchone()
            if row:
                cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (row[0],))
                word_count = cursor.fetchone()[0]
                return {
                    'id': row[0],
                    'name': row[1],
                    'user_id': row[2],
                    'created_at': row[3],
                    'updated_at': row[4],
                    'cloud_project_id': row[5],
                    'cloud_last_sync': row[6],
                    'migrated_to_cloud': row[7],
                    'word_count': word_count
                }
            return None
        finally:
            conn.close()

    # --- group level operations ---
    def rename_group(self, user_id, group_internal_id, new_name):
        print(f"DEBUG SM: rename_group called with user_id={user_id}, group_internal_id={group_internal_id}, new_name={new_name}")
        if not new_name or not new_name.strip():
            return False, "Project name is required"
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT user_id FROM project_groups WHERE id = ?
            """, (group_internal_id,))
            row = cursor.fetchone()
            if row and row[0] != user_id:
                print(f"DEBUG SM: rename_group Access denied for group {group_internal_id}")
                return False, "Access denied"
            if row:
                cursor.execute("""
                    UPDATE project_groups
                    SET name = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ? AND user_id = ?
                """, (new_name.strip(), group_internal_id, user_id))
            else:
                print(f"DEBUG SM: rename_group Group {group_internal_id} not found.")
                return False, "Group not found." # Group should exist to be renamed
            conn.commit()
            print(f"DEBUG SM: rename_group successfully renamed group {group_internal_id}")
            return True, None
        finally:
            conn.close()

    def _delete_local_project(self, project_id, user_id):
        print(f"DEBUG SM: _delete_local_project called for project_id={project_id}, user_id={user_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT name, cloud_project_id FROM projects WHERE id = ? AND user_id = ?
            """, (project_id, user_id))
            row = cursor.fetchone()
            if not row:
                print(f"DEBUG SM: _delete_local_project Project {project_id} not found")
                return False, "Project not found"
            project_name, cloud_project_id = row

            cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (project_id,))
            words_deleted = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM phonemes WHERE project_id = ?", (project_id,))
            phonemes_deleted = cursor.fetchone()[0]

            cursor.execute("DELETE FROM words WHERE project_id = ?", (project_id,))
            cursor.execute("DELETE FROM phonemes WHERE project_id = ?", (project_id,))
            cursor.execute("""
                DELETE FROM project_shares
                WHERE project_id = ? OR project_identifier = ?
            """, (project_id, f'local:{project_id}'))
            if cloud_project_id:
                cursor.execute("DELETE FROM project_shares WHERE cloud_project_id = ?", (cloud_project_id,))

            cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
            conn.commit()
            print(f"DEBUG SM: _delete_local_project successfully deleted project {project_id}")
            return True, {
                'name': project_name,
                'words_deleted': words_deleted,
                'phonemes_deleted': phonemes_deleted
            }
        finally:
            conn.close()

    def _delete_cloud_project(self, cloud_project_id, user_id):
        print(f"DEBUG SM: _delete_cloud_project called for cloud_project_id={cloud_project_id}, user_id={user_id}")
        if not clean_firebase_service.is_available():
            print("DEBUG SM: _delete_cloud_project Cloud storage not available")
            return False, "Cloud storage is not available"
        project_meta = self._fetch_project_metadata('cloud', cloud_project_id, owner_id=user_id)
        if not project_meta:
            print(f"DEBUG SM: _delete_cloud_project Cloud project {cloud_project_id} not found or access denied")
            return False, "Project not found or access denied"

        try:
            firestore_db.delete_project_words(cloud_project_id)
            firestore_db.delete_project_phonemes(cloud_project_id)
            firestore_db.delete_project(cloud_project_id)
            print(f"DEBUG SM: _delete_cloud_project successfully deleted cloud project {cloud_project_id} from Firestore")
        except Exception as exc:
            print(f"DEBUG SM: _delete_cloud_project Error deleting cloud project {cloud_project_id} from Firestore: {exc}")
            return False, str(exc)

        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM project_shares
                WHERE project_identifier = ? OR cloud_project_id = ?
            """, (f'cloud:{cloud_project_id}', cloud_project_id))
            conn.commit()
            print(f"DEBUG SM: _delete_cloud_project deleted project_shares for {cloud_project_id}")
        finally:
            conn.close()

        return True, {
            'name': project_meta.get('name', cloud_project_id)
        }

    def delete_group(self, user_id, group_internal_id): # group_internal_id is the INTEGER ID
        print(f"DEBUG SM: delete_group called for user_id={user_id}, group_internal_id={group_internal_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id FROM project_groups
                WHERE parent_group_id = ? AND user_id = ?
            """, (group_internal_id, user_id))
            child_groups = [row[0] for row in cursor.fetchall()]
            print(f"DEBUG SM: delete_group found {len(child_groups)} child groups for {group_internal_id}")
            cursor.execute("""
                SELECT variant_identifier, storage_type
                FROM project_variants_meta
                WHERE group_id = ? AND user_id = ?
            """, (group_internal_id, user_id))
            variants = cursor.fetchall()
            print(f"DEBUG SM: delete_group found {len(variants)} variants for group {group_internal_id}")
        finally:
            conn.close()

        for child_id in child_groups:
            ok, info = self.delete_group(user_id, child_id)
            if not ok:
                return False, info

        deleted_variants = []
        for variant_identifier, storage_type in variants:
            if not variant_identifier:
                continue
            prefix, ident = variant_identifier.split(':', 1)
            if storage_type == 'local' or prefix == 'local':
                ok, info = self._delete_local_project(int(ident), user_id)
            else:
                ok, info = self._delete_cloud_project(ident, user_id)
            if ok:
                deleted_variants.append({'variant_identifier': variant_identifier, 'details': info})
                conn = self._connect()
                try:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM project_variants_meta WHERE variant_identifier = ?", (variant_identifier,))
                    conn.commit()
                finally:
                    conn.close()
            else:
                return False, info

        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM project_groups WHERE id = ? AND user_id = ?", (group_internal_id, user_id))
            conn.commit()
            print(f"DEBUG SM: delete_group successfully deleted group {group_internal_id}")
        finally:
            conn.close()

        return True, deleted_variants

    def _copy_local_to_local(self, source_project_id, target_project_id, user_id):
        print(f"DEBUG SM: _copy_local_to_local called source={source_project_id}, target={target_project_id}, user_id={user_id}")
        self._ensure_column_cache()
        conn = self._connect()
        try:
            cursor = conn.cursor()

            word_columns = [col for col in self._words_columns if col != 'id']
            placeholders = ",".join(["?"] * len(word_columns))
            cursor.execute(f"SELECT {', '.join(word_columns)} FROM words WHERE project_id = ?", (source_project_id,))
            for row in cursor.fetchall():
                row_values = list(row)
                values_by_col = dict(zip(word_columns, row_values))
                values = []
                for col in word_columns:
                    if col == 'project_id':
                        values.append(target_project_id)
                    elif col == 'user_id':
                        values.append(user_id)
                    else:
                        values.append(values_by_col.get(col))
                cursor.execute(
                    f"INSERT INTO words ({', '.join(word_columns)}) VALUES ({placeholders})",
                    values
                )

            phoneme_columns = [col for col in self._phoneme_columns if col != 'id']
            phoneme_placeholders = ",".join(["?"] * len(phoneme_columns))
            cursor.execute(f"SELECT {', '.join(phoneme_columns)} FROM phonemes WHERE project_id = ?", (source_project_id,))
            for row in cursor.fetchall():
                row_values = list(row)
                values_by_col = dict(zip(phoneme_columns, row_values))
                values = []
                for col in phoneme_columns:
                    if col == 'project_id':
                        values.append(target_project_id)
                    elif col == 'user_id':
                        values.append(user_id)
                    else:
                        values.append(values_by_col.get(col))
                cursor.execute(
                    f"INSERT INTO phonemes ({', '.join(phoneme_columns)}) VALUES ({phoneme_placeholders})",
                    values
                )

            conn.commit()
            print(f"DEBUG SM: _copy_local_to_local successfully copied data from {source_project_id} to {target_project_id}")
        finally:
            conn.close()

    def branch_variant(self, user_id, base_variant_identifier, branch_name, target_storage=StorageType.LOCAL):
        print(f"DEBUG SM: branch_variant called with user_id={user_id}, base_variant_identifier={base_variant_identifier}, branch_name={branch_name}")
        if not base_variant_identifier:
            return False, "Invalid base variant"
        branch_name = (branch_name or '').strip()
        prefix, ident = base_variant_identifier.split(':', 1)
        storage_label = prefix
        
        # Get integer group_id for the base variant
        base_meta = self._get_variant_metadata(base_variant_identifier, user_id)
        base_group_internal_id = base_meta['group_id'] if base_meta else None
        if base_group_internal_id is None:
            # If variant metadata not found, ensure a group exists for the identifier
            base_group_meta = self._ensure_group_metadata(base_variant_identifier, "Base Variant", user_id)
            base_group_internal_id = base_group_meta['group_id']

        if target_storage != StorageType.LOCAL:
            return False, "Only local branches are currently supported"

        if storage_label == 'local':
            conn = self._connect()
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT name FROM projects WHERE id = ? AND user_id = ?
                """, (int(ident), user_id))
                row = cursor.fetchone()
            finally:
                conn.close()
            if not row:
                return False, "Base project not found"
            base_name = row[0]
            new_name = branch_name or f"{base_name} (branch)"
            project_data = {
                'name': new_name,
                'user_id': user_id,
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
            }
            new_project_id = self._create_project_sqlite(project_data)
            self._copy_local_to_local(int(ident), new_project_id, user_id)
            new_variant_identifier = self._variant_key('local', new_project_id)
        else:
            if not clean_firebase_service.is_available():
                return False, "Cloud storage is not available"
            base_meta_cloud = self._fetch_project_metadata('cloud', ident, owner_id=user_id)
            if not base_meta_cloud:
                return False, "Cloud project not found or access denied"
            base_name = base_meta_cloud.get('name', 'Cloud Project')
            new_name = branch_name or f"{base_name} (branch)"
            project_data = {
                'name': new_name,
                'user_id': user_id,
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
            }
            new_project_id = self._create_project_sqlite(project_data)
            self._copy_cloud_to_local(ident, new_project_id, user_id)
            new_variant_identifier = self._variant_key('local', new_project_id)

        # Ensure a group for the new variant, potentially linking to base_group_internal_id as parent
        new_group_meta = self._ensure_group_metadata(new_variant_identifier, new_name, user_id, parent_group_id=base_group_internal_id)
        new_group_internal_id = new_group_meta['group_id']

        # Ensure metadata for the new variant
        self._ensure_variant_metadata(
            new_variant_identifier,
            new_group_internal_id, # Pass the INTEGER group_id
            'local',
            user_id,
            default_branch_name=branch_name or 'branch',
            parent_identifier=base_variant_identifier
        )
        print(f"DEBUG SM: branch_variant returning success for new_variant_identifier={new_variant_identifier}, group_id={new_group_internal_id}")
        return True, {'variant_identifier': new_variant_identifier, 'group_id': new_group_internal_id}

    def merge_variants(self, user_id, source_variant_identifier, target_variant_identifier):
        """Merge data from source variant into target variant (overwrite strategy)."""
        print(f"DEBUG SM: merge_variants called user_id={user_id}, source={source_variant_identifier}, target={target_variant_identifier}")
        if not source_variant_identifier or not target_variant_identifier:
            return False, "Both source and target variants are required for a merge."
        if source_variant_identifier == target_variant_identifier:
            return False, "Cannot merge a variant into itself."

        try:
            source_prefix, source_id = source_variant_identifier.split(':', 1)
            target_prefix, target_id = target_variant_identifier.split(':', 1)
        except ValueError:
            return False, "Invalid variant identifiers."

        if source_prefix != 'local' or target_prefix != 'local':
            return False, "Merging is currently supported only for local variants."

        try:
            source_int = int(source_id)
            target_int = int(target_id)
        except (TypeError, ValueError):
            return False, "Invalid local variant identifiers."

        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT user_id, name FROM projects WHERE id = ?", (source_int,))
            source_row = cursor.fetchone()
            if not source_row:
                return False, "Source variant not found."
            if source_row[0] != user_id:
                return False, "Access denied for source variant."
            source_name = source_row[1]

            cursor.execute("SELECT user_id, name FROM projects WHERE id = ?", (target_int,))
            target_row = cursor.fetchone()
            if not target_row:
                return False, "Target variant not found."
            if target_row[0] != user_id:
                return False, "Access denied for target variant."
            target_name = target_row[1]

            cursor.execute("DELETE FROM words WHERE project_id = ?", (target_int,))
            cursor.execute("DELETE FROM phonemes WHERE project_id = ?", (target_int,))
            cursor.execute("""
                UPDATE projects
                SET updated_at = ?
                WHERE id = ?
            """, (datetime.utcnow(), target_int))
            conn.commit()
        finally:
            conn.close()

        self._copy_local_to_local(source_int, target_int, user_id)

        message = f'Merged "{source_name}" into "{target_name}" successfully.'
        print(f"DEBUG SM: merge_variants successfully merged {source_variant_identifier} into {target_variant_identifier}")
        return True, message

    def delete_variant(self, user_id, variant_identifier):
        print(f"DEBUG SM: delete_variant called user_id={user_id}, variant_identifier={variant_identifier}")
        if not variant_identifier:
            return False, "Invalid project identifier"
        prefix, ident = variant_identifier.split(':', 1)
        if prefix == 'local':
            ok, info = self._delete_local_project(int(ident), user_id)
        else:
            ok, info = self._delete_cloud_project(ident, user_id)
        if ok:
            conn = self._connect()
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM project_variants_meta WHERE variant_identifier = ?", (variant_identifier,))
                conn.commit()
                print(f"DEBUG SM: delete_variant deleted project_variants_meta for {variant_identifier}")
            finally:
                conn.close()
            details = info if isinstance(info, dict) else {'name': info}
            words_deleted = details.get('words_deleted')
            phonemes_deleted = details.get('phonemes_deleted')
            if words_deleted is not None and phonemes_deleted is not None:
                message = f'Project "{details.get("name", variant_identifier)}" deleted successfully! Removed {words_deleted} words and {phonemes_deleted} phonemes.'
            else:
                message = f'Project "{details.get("name", variant_identifier)}" deleted successfully.'
            return True, message
        return ok, (info if isinstance(info, str) else str(info))

    def get_group_detail(self, group_id, user_id):
        print(f"DEBUG SM: get_group_detail called group_id={group_id}, user_id={user_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()

            # Get group basic details
            cursor.execute("""
                SELECT id, name, description, user_id FROM project_groups
                WHERE id = ?
            """, (group_id,))
            group_row = cursor.fetchone()

            if not group_row:
                print(f"DEBUG SM: get_group_detail Group {group_id} not found.")
                return None

            group_internal_id, name, description, admin_user_id = group_row
            
            # Check membership
            cursor.execute("""
                SELECT COUNT(*) FROM group_memberships
                WHERE group_id = ? AND user_id = ?
            """, (group_id, user_id))
            is_member = cursor.fetchone()[0] > 0

            # Determine if user is admin
            is_admin = (admin_user_id == user_id)

            group_detail = {
                'id': group_internal_id,
                'name': name,
                'description': description,
                'admin_user_id': admin_user_id,
                'is_member': is_member,
                'is_admin': is_admin
            }
            print(f"DEBUG SM: get_group_detail returning: {group_detail}")
            return group_detail
        finally:
            conn.close()

    def get_projects_shared_with_group(self, group_id, user_id):
        print(f"DEBUG SM: get_projects_shared_with_group called group_id={group_id}, user_id={user_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()
            
            # First, verify user is a member of the group
            cursor.execute("""
                SELECT COUNT(*) FROM group_memberships
                WHERE group_id = ? AND user_id = ?
            """, (group_id, user_id))
            if cursor.fetchone()[0] == 0:
                print(f"DEBUG SM: get_projects_shared_with_group User {user_id} is not a member of group {group_id}.")
                return [] # User not a member

            # Fetch projects shared with this group
            cursor.execute("""
                SELECT ps.project_id, ps.project_identifier, ps.storage_type
                FROM project_shares ps
                WHERE ps.group_id = ?
            """, (group_id,))
            shared_project_identifiers = cursor.fetchall()

            shared_projects_data = []
            for project_sqlite_id, project_identifier, storage_type in shared_project_identifiers:
                prefix, ident = project_identifier.split(':', 1)
                
                # Fetch project details based on its storage type
                if storage_type == 'local' and prefix == 'local':
                    # For local SQLite projects, use _get_project_sqlite_by_id
                    project_detail = self._get_project_sqlite_by_id(int(ident))
                    if project_detail:
                        project_detail['storage_type'] = 'local'
                        shared_projects_data.append(project_detail)
                elif storage_type == 'cloud' and prefix == 'cloud':
                    # For cloud Firestore projects, use firestore_db
                    if clean_firebase_service.is_available():
                        cloud_project_detail = firestore_db.get_project(ident)
                        if cloud_project_detail:
                            cloud_project_detail['storage_type'] = 'cloud'
                            shared_projects_data.append(cloud_project_detail)
            
            # Sort by updated_at if available
            shared_projects_data.sort(key=lambda p: self._parse_datetime(p.get('updated_at')) or datetime.min.replace(tzinfo=timezone.utc), reverse=True)

            print(f"DEBUG SM: get_projects_shared_with_group returning {len(shared_projects_data)} projects for group {group_id}")
            return shared_projects_data
        finally:
            conn.close()

    def get_variant_metadata(self, user_id, variant_identifier):
        print(f"DEBUG SM: get_variant_metadata called user_id={user_id}, variant_identifier={variant_identifier}")
        return self._get_variant_metadata(variant_identifier, user_id)
    
    def get_cloud_project_id(self, project_id, user_id):
        """Return the associated cloud project id for a given local project if available."""
        print(f"DEBUG SM: get_cloud_project_id called project_id={project_id}, user_id={user_id}")
        if project_id is None:
            return None
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT cloud_project_id
                FROM projects
                WHERE id = ? AND user_id = ?
            """, (project_id, user_id))
            row = cursor.fetchone()
            if row:
                return row[0]
            return None
        finally:
            conn.close()

    def create_cloud_word(self, cloud_project_id, word_payload):
        """Create a word document in Firestore for a cloud project."""
        print(f"DEBUG SM: create_cloud_word called cloud_project_id={cloud_project_id}, word_payload={word_payload}")
        if not cloud_project_id or not clean_firebase_service.is_available():
            return None
        payload = dict(word_payload or {})
        payload["project_id"] = cloud_project_id
        now = datetime.utcnow()
        payload.setdefault("created_at", now)
        payload.setdefault("updated_at", payload["created_at"])
        return firestore_db.create_word(payload)

    def increment_cloud_phoneme_frequency(self, cloud_project_id, phoneme_record, increment=1):
        """Ensure a phoneme document exists for the cloud project and increment its frequency."""
        print(f"DEBUG SM: increment_cloud_phoneme_frequency called cloud_project_id={cloud_project_id}, phoneme_record={phoneme_record}, increment={increment}")
        if not cloud_project_id or not clean_firebase_service.is_available() or not phoneme_record:
            return

        try:
            conditions = [
                ("project_id", "==", cloud_project_id),
                ("syllable_type", "==", phoneme_record.get("syllable_type")),
                ("position", "==", phoneme_record.get("position")),
                ("length_type", "==", phoneme_record.get("length_type")),
                ("phoneme", "==", phoneme_record.get("phoneme")),
            ]
            matches = firestore_db.get_documents(
                firestore_db.PHONEMES_COLLECTION,
                where_conditions=conditions,
                limit=1,
            )
            now = datetime.utcnow()
            if matches:
                doc = matches[0]
                current_frequency = int(doc.get("frequency", 0) or 0)
                firestore_db.update_phoneme(doc["id"], {
                    "frequency": current_frequency + int(increment),
                    "updated_at": now,
                })
                print(f"DEBUG SM: increment_cloud_phoneme_frequency updated existing phoneme: {doc['id']}")
            else:
                firestore_db.create_phoneme({
                    "phoneme": phoneme_record.get("phoneme"),
                    "language": phoneme_record.get("language"),
                    "frequency": int(increment),
                    "syllable_type": phoneme_record.get("syllable_type"),
                    "position": phoneme_record.get("position"),
                    "length_type": phoneme_record.get("length_type"),
                    "group_type": phoneme_record.get("group_type"),
                    "subgroup_type": phoneme_record.get("subgroup_type"),
                    "sub_subgroup_type": phoneme_record.get("sub_subgroup_type"),
                    "sub_sub_subgroup_type": phoneme_record.get("sub_sub_subgroup_type"),
                    "project_id": cloud_project_id,
                    "user_id": phoneme_record.get("user_id"),
                    "created_at": now,
                    "updated_at": now,
                })
                print(f"DEBUG SM: increment_cloud_phoneme_frequency created new phoneme for cloud project: {cloud_project_id}")
        except Exception as exc:
            print(f"DEBUG SM: increment_cloud_phoneme_frequency Error updating cloud phoneme frequency: {exc}")
    
    def migrate_project_to_cloud(self, project_id, user_id):
        """Migrate a local project to cloud storage"""
        print(f"DEBUG SM: migrate_project_to_cloud called project_id={project_id}, user_id={user_id}")
        if not clean_firebase_service.is_available():
            print("DEBUG SM: migrate_project_to_cloud Cloud storage not available")
            return False, "Cloud storage not available"

        try:
            conn = self._connect()
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, name, user_id, created_at, updated_at
                    FROM projects WHERE id = ? AND user_id = ?
                """, (project_id, user_id))

                project_row = cursor.fetchone()
                if not project_row:
                    print(f"DEBUG SM: migrate_project_to_cloud Project {project_id} not found")
                    return False, "Project not found"

                # Snapshot local counts before migration for verification
                cursor.execute("SELECT COUNT(*) FROM words WHERE project_id = ?", (project_id,))
                local_word_count = int(cursor.fetchone()[0])
                cursor.execute("SELECT COUNT(*) FROM phonemes WHERE project_id = ?", (project_id,))
                local_phoneme_count = int(cursor.fetchone()[0])
                print(f"DEBUG SM: migrate_project_to_cloud local counts: words={local_word_count}, phonemes={local_phoneme_count}")

                project_data = {
                    'name': project_row[1],
                    'user_id': user_id,
                    'created_at': datetime.fromisoformat(project_row[3]) if project_row[3] else datetime.utcnow(),
                    'updated_at': datetime.utcnow(),
                    'migrated_from_sqlite': True,
                    'original_sqlite_id': project_row[0],
                    'firebase_uid': self._get_user_firebase_uid(user_id),
                }

                cloud_project_id = firestore_db.create_project(project_data)
                if not cloud_project_id:
                    print("DEBUG SM: migrate_project_to_cloud Failed to create cloud project")
                    return False, "Failed to create cloud project"
                print(f"DEBUG SM: migrate_project_to_cloud created cloud_project_id={cloud_project_id}")

                # Confirm cloud project exists before proceeding
                if not firestore_db.get_project(cloud_project_id):
                    print("DEBUG SM: migrate_project_to_cloud Cloud project write not confirmed")
                    return False, "Cloud project write not confirmed"

                local_variant_identifier = self._variant_key('local', project_id)
                local_meta = self._get_variant_metadata(local_variant_identifier, user_id)
                
                # Get integer group_id for the base variant
                group_meta_for_local_root = self._ensure_group_metadata(local_variant_identifier, project_data['name'], user_id)
                group_internal_id = group_meta_for_local_root['group_id'] # This is the INTEGER ID
                
                self._ensure_variant_metadata(
                    local_variant_identifier,
                    group_internal_id, # Pass the INTEGER group_id
                    'local',
                    user_id,
                    default_branch_name=local_meta['branch_name'] if local_meta and local_meta.get('branch_name') else 'main',
                    parent_identifier=None # Local variant as root for migration
                )
                cloud_variant_identifier = self._variant_key('cloud', cloud_project_id)
                self._ensure_variant_metadata(
                    cloud_variant_identifier,
                    group_internal_id, # Pass the INTEGER group_id
                    'cloud',
                    user_id,
                    default_branch_name=local_meta['branch_name'] if local_meta and local_meta.get('branch_name') else 'main',
                    parent_identifier=local_variant_identifier
                )

                # Execute the data migration (words and phonemes)
                self._migrate_project_data(project_id, cloud_project_id, user_id)

                # Verify migrated counts match (depth-first slice verification)
                cloud_word_count = int(firestore_db.count_project_words(cloud_project_id))
                cloud_phoneme_count = int(len(firestore_db.get_project_phonemes(cloud_project_id)))
                print(f"DEBUG SM: migrate_project_to_cloud cloud counts: words={cloud_word_count}, phonemes={cloud_phoneme_count}")
                if cloud_word_count != local_word_count or cloud_phoneme_count != local_phoneme_count:
                    print(f"DEBUG SM: migrate_project_to_cloud Migration incomplete: expected {local_word_count} words/{local_phoneme_count} phonemes, found {cloud_word_count}/{cloud_phoneme_count} in cloud")
                    return False, (
                        f"Migration incomplete: expected {local_word_count} words/{local_phoneme_count} phonemes, "
                        f"found {cloud_word_count}/{cloud_phoneme_count} in cloud"
                    )

                # Only update local linkage if cloud verification passed
                now_iso = datetime.utcnow().isoformat()
                cursor.execute("""
                    UPDATE projects SET updated_at = ?, migrated_to_cloud = ?, cloud_project_id = ?, cloud_last_sync = ?
                    WHERE id = ?
                """, (now_iso, 1, cloud_project_id, now_iso, project_id))

                conn.commit()
                print(f"DEBUG SM: migrate_project_to_cloud successfully migrated project {project_id} to cloud (ID: {cloud_project_id})")
            finally:
                conn.close()

            return True, f"Project migrated successfully to cloud (ID: {cloud_project_id})"

        except Exception as e:
            print(f"DEBUG SM: migrate_project_to_cloud Migration failed: {e}")
            return False, f"Migration failed: {e}"
    
    def _migrate_project_data(self, sqlite_project_id, cloud_project_id, user_id):
        """Push local words and phonemes for a project into the cloud project."""
        print(f"DEBUG SM: _migrate_project_data called sqlite_project_id={sqlite_project_id}, cloud_project_id={cloud_project_id}, user_id={user_id}")
        if not cloud_project_id:
            return
        if not clean_firebase_service.is_available():
            return

        self._ensure_column_cache()

        # Always start from a clean slate to avoid duplicated cloud entries.
        firestore_db.delete_project_words(cloud_project_id)
        firestore_db.delete_project_phonemes(cloud_project_id)
        print(f"DEBUG SM: _migrate_project_data cleared cloud data for {cloud_project_id}")

        conn = self._connect()
        try:
            cursor = conn.cursor()

            word_columns = [col for col in self._words_columns if col != 'id']
            if word_columns:
                cursor.execute(
                    f"SELECT {', '.join(word_columns)} FROM words WHERE project_id = ?",
                    (sqlite_project_id,),
                )
                for row in cursor.fetchall():
                    values_by_col = dict(zip(word_columns, row))
                    english_words = self._deserialize_english_words(values_by_col.get('english_words'))
                    firestore_db.create_word({
                        'language': values_by_col.get('language'),
                        'english_words': english_words,
                        'new_language_word': values_by_col.get('new_language_word'),
                        'ipa_phonetics': values_by_col.get('ipa_phonetics'),
                        'dictionary_phonetics': values_by_col.get('dictionary_phonetics'),
                        'video_path': values_by_col.get('video_path'),
                        'syllable_type': values_by_col.get('syllable_type'),
                        'onset_phoneme': values_by_col.get('onset_phoneme'),
                        'onset_length_type': values_by_col.get('onset_length_type'),
                        'nucleus_phoneme': values_by_col.get('nucleus_phoneme'),
                        'nucleus_length_type': values_by_col.get('nucleus_length_type'),
                        'coda_phoneme': values_by_col.get('coda_phoneme'),
                        'coda_length_type': values_by_col.get('coda_length_type'),
                        'user_id': values_by_col.get('user_id') or user_id,
                        'project_id': cloud_project_id,
                        'created_at': values_by_col.get('created_at'),
                        'updated_at': values_by_col.get('updated_at'),
                    })
                print(f"DEBUG SM: _migrate_project_data migrated words for project {sqlite_project_id}")

            phoneme_columns = [col for col in self._phoneme_columns if col != 'id']
            if phoneme_columns:
                cursor.execute(
                    f"SELECT {', '.join(phoneme_columns)} FROM phonemes WHERE project_id = ?",
                    (sqlite_project_id,),
                    )
                for row in cursor.fetchall():
                    values_by_col = dict(zip(phoneme_columns, row))
                    firestore_db.create_phoneme({
                        'syllable_type': values_by_col.get('syllable_type'),
                        'position': values_by_col.get('position'),
                        'length_type': values_by_col.get('length_type'),
                        'group_type': values_by_col.get('group_type'),
                        'subgroup_type': values_by_col.get('subgroup_type'),
                        'sub_subgroup_type': values_by_col.get('sub_subgroup_type'),
                        'sub_sub_subgroup_type': values_by_col.get('sub_sub_subgroup_type'),
                        'phoneme': values_by_col.get('phoneme'),
                        'frequency': values_by_col.get('frequency'),
                        'language': values_by_col.get('language'),
                        'project_id': cloud_project_id,
                        'user_id': values_by_col.get('user_id') or user_id,
                        'created_at': values_by_col.get('created_at'),
                        'updated_at': values_by_col.get('updated_at'),
                    })
                print(f"DEBUG SM: _migrate_project_data migrated phonemes for project {sqlite_project_id}")
        finally:
            conn.close()

    # --- synchronization helpers ---
    def _get_table_columns(self, table_name):
        conn = self._connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"PRAGMA table_info({table_name})")
            return [row[1] for row in cursor.fetchall()]
        finally:
            conn.close()

    def _ensure_column_cache(self):
        # Lazy load: check if already loaded
        if (getattr(self, '_words_columns', None) is not None and
            getattr(self, '_phoneme_columns', None) is not None and
            getattr(self, '_project_columns', None) is not None):
            return

        # Attempt to load columns, gracefully handle failures during init/tests
        try:
            if getattr(self, '_words_columns', None) is None:
                self._words_columns = self._get_table_columns('words')
            if getattr(self, '_phoneme_columns', None) is None:
                self._phoneme_columns = self._get_table_columns('phonemes')
            if getattr(self, '_project_columns', None) is None:
                self._project_columns = self._get_table_columns('projects')
        except Exception as e:
            # During tests/migrations, tables might not exist yet
            # print(f"Warning: Failed to cache columns: {e}")
            pass

    def _parse_datetime(self, value):
        if not value:
            return None

        if isinstance(value, str):
            try:
                v = value.strip()
                if not v:
                    return None
                if v.endswith('Z'):
                    v = v[:-1] + '+00:00'
                dt = datetime.fromisoformat(v)
            except Exception:
                return None
        elif isinstance(value, datetime):
            dt = value
        else:
            return None

        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        else:
            dt = dt.astimezone(timezone.utc)
        return dt

    def _to_iso(self, value):
        dt = self._parse_datetime(value)
        if dt:
            return dt.isoformat()
        if isinstance(value, str):
            return value
        return ''

    def _format_display(self, value):
        dt = self._parse_datetime(value)
        if not dt:
            return None
        return dt.strftime('%Y-%m-%d %H:%M')

    def _deserialize_english_words(self, value):
        if value is None:
            return []
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            try:
                loaded = json.loads(value)
                if isinstance(loaded, list):
                    return loaded
                if isinstance(loaded, str):
                    return [loaded]
            except json.JSONDecodeError:
                stripped = value.strip()
                if stripped.startswith('[') and stripped.endswith(']'):
                    try:
                        loaded = json.loads(stripped)
                        if isinstance(loaded, list):
                            return loaded
                    except json.JSONDecodeError:
                        pass
                if stripped:
                    return [stripped]
            return []
        return [str(value)]

    def _serialize_english_words(self, value):
        if value is None:
            return json.dumps([])
        if isinstance(value, list):
            return json.dumps(value)
        if isinstance(value, str):
            try:
                loaded = json.loads(value)
                if isinstance(loaded, list):
                    return json.dumps(loaded)
            except json.JSONDecodeError:
                pass
            return json.dumps([value])
        return json.dumps([value])

    def _clear_local_project_data(self, project_id):
        print(f"DEBUG SM: _clear_local_project_data called project_id={project_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM words WHERE project_id = ?", (project_id,))
            cursor.execute("DELETE FROM phonemes WHERE project_id = ?", (project_id,))
            conn.commit()
            print(f"DEBUG SM: _clear_local_project_data cleared data for project {project_id}")
        finally:
            conn.close()

    def _clear_cloud_project_data(self, cloud_project_id):
        print(f"DEBUG SM: _clear_cloud_project_data called cloud_project_id={cloud_project_id}")
        firestore_db.delete_project_words(cloud_project_id)
        firestore_db.delete_project_phonemes(cloud_project_id)
        print(f"DEBUG SM: _clear_cloud_project_data cleared cloud data for {cloud_project_id}")

    def _copy_cloud_to_local(self, cloud_project_id, sqlite_project_id, user_id):
        print(f"DEBUG SM: _copy_cloud_to_local called cloud={cloud_project_id}, sqlite={sqlite_project_id}, user_id={user_id}")
        self._ensure_column_cache()
        conn = self._connect()
        try:
            cursor = conn.cursor()

            words = firestore_db.get_project_words(cloud_project_id)
            word_columns = [
                'language', 'english_words', 'new_language_word', 'ipa_phonetics',
                'dictionary_phonetics', 'syllable_type', 'onset_phoneme', 'onset_length_type',
                'nucleus_phoneme', 'nucleus_length_type', 'coda_phoneme', 'coda_length_type',
                'video_path', 'project_id'
            ]
            for word in words:
                english_words_val = self._serialize_english_words(word.get('english_words'))

                row = [
                    word.get('language'),
                    english_words_val,
                    word.get('new_language_word'),
                    word.get('ipa_phonetics'),
                    word.get('dictionary_phonetics'),
                    word.get('syllable_type'),
                    word.get('onset_phoneme'),
                    word.get('onset_length_type'),
                    word.get('nucleus_phoneme'),
                    word.get('nucleus_length_type'),
                    word.get('coda_phoneme'),
                    word.get('coda_length_type'),
                    word.get('video_path'),
                    sqlite_project_id
                ]
                columns = list(word_columns)
                values = list(row)
                if 'user_id' in self._words_columns:
                    columns.append('user_id')
                    values.append(user_id)
                if 'created_at' in self._words_columns and word.get('created_at'):
                    columns.append('created_at')
                    created_at = word.get('created_at')
                    if hasattr(created_at, 'isoformat'):
                        created_at = created_at.isoformat()
                    values.append(created_at)
                if 'updated_at' in self._words_columns and word.get('updated_at'):
                    columns.append('updated_at')
                    updated_at = word.get('updated_at')
                    if hasattr(updated_at, 'isoformat'):
                        updated_at = updated_at.isoformat()
                    values.append(updated_at)

                placeholders = ",".join(["?"] * len(values))
                cursor.execute(
                    f"INSERT INTO words ({', '.join(columns)}) VALUES ({placeholders})",
                    values
                )

            phonemes = firestore_db.get_project_phonemes(cloud_project_id)
            phoneme_columns = [
                'syllable_type', 'position', 'length_type', 'group_type',
                'subgroup_type', 'sub_subgroup_type', 'sub_sub_subgroup_type',
                'phoneme', 'frequency', 'project_id'
            ]

            for phoneme in phonemes:
                row = [
                    phoneme.get('syllable_type'),
                    phoneme.get('position'),
                    phoneme.get('length_type'),
                    phoneme.get('group_type'),
                    phoneme.get('subgroup_type'),
                    phoneme.get('sub_subgroup_type'),
                    phoneme.get('sub_sub_subgroup_type'),
                    phoneme.get('phoneme'),
                    int(phoneme.get('frequency', 0) or 0),
                    sqlite_project_id
                ]
                columns = list(phoneme_columns)
                values = list(row)
                if 'user_id' in self._phoneme_columns:
                    columns.append('user_id')
                    values.append(user_id)

                placeholders = ",".join(["?"] * len(values))
                cursor.execute(
                    f"INSERT INTO phonemes ({', '.join(columns)}) VALUES ({placeholders})",
                    values
                )

            conn.commit()
            print(f"DEBUG SM: _copy_cloud_to_local successfully copied data from cloud {cloud_project_id} to local {sqlite_project_id}")
        finally:
            conn.close()

    def _update_local_project_sync(self, project_id, cloud_project_id=None):
        print(f"DEBUG SM: _update_local_project_sync called project_id={project_id}, cloud_project_id={cloud_project_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()
            now_iso = datetime.utcnow().isoformat()
            if cloud_project_id is not None:
                cursor.execute("""
                    UPDATE projects
                    SET cloud_project_id = ?, cloud_last_sync = ?, updated_at = ?, migrated_to_cloud = 1
                    WHERE id = ?
                """, (cloud_project_id, now_iso, now_iso, project_id))
            else:
                cursor.execute("""
                    UPDATE projects
                    SET cloud_last_sync = ?, updated_at = ?
                    WHERE id = ?
                """, (now_iso, now_iso, project_id))
            conn.commit()
            print(f"DEBUG SM: _update_local_project_sync updated local project {project_id}")
        finally:
            conn.close()

    def touch_local_project(self, project_id):
        print(f"DEBUG SM: touch_local_project called project_id={project_id}")
        conn = self._connect()
        try:
            cursor = conn.cursor()
            now_iso = datetime.utcnow().isoformat()
            cursor.execute("UPDATE projects SET updated_at = ? WHERE id = ?", (now_iso, project_id))
            conn.commit()
            print(f"DEBUG SM: touch_local_project updated updated_at for project {project_id}")
        finally:
            conn.close()

    def fork_cloud_project_to_local(self, cloud_project_id, user_id, new_name=None):
        print(f"DEBUG SM: fork_cloud_project_to_local called cloud_project_id={cloud_project_id}, user_id={user_id}, new_name={new_name}")
        if not clean_firebase_service.is_available():
            print("DEBUG SM: fork_cloud_project_to_local Cloud storage not available")
            return False, "Cloud storage not available"

        try:
            project_doc = firestore_db.get_project(cloud_project_id)
            if not project_doc:
                print(f"DEBUG SM: fork_cloud_project_to_local Cloud project {cloud_project_id} not found")
                return False, "Cloud project not found"

            owner_id = project_doc.get('user_id') or project_doc.get('user_id_str')
            if owner_id is not None and str(owner_id) != str(user_id):
                print(f"DEBUG SM: fork_cloud_project_to_local Access denied for cloud project {cloud_project_id}")
                return False, "Access denied for this project"

            project_name = new_name.strip() if new_name and new_name.strip() else project_doc.get('name', 'Cloud Project')
            project_data = {
                'name': project_name,
                'user_id': user_id,
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                'cloud_project_id': cloud_project_id,
                'cloud_last_sync': datetime.utcnow()
            }
            local_project_id = self._create_project_sqlite(project_data)
            self._clear_local_project_data(local_project_id)
            self._copy_cloud_to_local(cloud_project_id, local_project_id, user_id)
            self._update_local_project_sync(local_project_id, cloud_project_id)
            cloud_variant_identifier = self._variant_key('cloud', cloud_project_id)
            cloud_meta = self._get_variant_metadata(cloud_variant_identifier, user_id)
            
            # Ensure a group exists for the cloud variant identifier to get its integer ID
            group_meta_for_cloud_root = self._ensure_group_metadata(cloud_variant_identifier, project_name, user_id)
            group_internal_id = group_meta_for_cloud_root['group_id']

            self._ensure_variant_metadata(
                local_variant_identifier,
                group_internal_id, # Pass the INTEGER group_id
                'local',
                user_id,
                default_branch_name='branch',
                parent_identifier=cloud_variant_identifier
            )
            print(f"DEBUG SM: fork_cloud_project_to_local successfully forked cloud project {cloud_project_id} to local {local_project_id}")
            return True, local_project_id
        except Exception as exc:
            print(f"DEBUG SM: fork_cloud_project_to_local Fork failed: {exc}")
            return False, f"Fork failed: {exc}"

    def sync_local_to_cloud(self, project_id, user_id):
        print(f"DEBUG SM: sync_local_to_cloud called project_id={project_id}, user_id={user_id}")
        if not clean_firebase_service.is_available():
            print("DEBUG SM: sync_local_to_cloud Cloud storage not available")
            return False, "Cloud storage not available"

        try:
            conn = self._connect()
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, name, cloud_project_id
                    FROM projects
                    WHERE id = ? AND user_id = ?
                """, (project_id, user_id))
                row = cursor.fetchone()
            finally:
                conn.close()

            if not row:
                print(f"DEBUG SM: sync_local_to_cloud Project {project_id} not found")
                return False, "Project not found"

            cloud_project_id = row[2]
            if not cloud_project_id:
                print(f"DEBUG SM: sync_local_to_cloud Migrating project {project_id} to cloud")
                success, message = self.migrate_project_to_cloud(project_id, user_id)
                return success, message

            self._migrate_project_data(project_id, cloud_project_id, user_id)
            self._update_local_project_sync(project_id)
            print(f"DEBUG SM: sync_local_to_cloud successfully synced local project {project_id} to cloud {cloud_project_id}")
            return True, "Cloud project updated from local data"
        except Exception as exc:
            print(f"DEBUG SM: sync_local_to_cloud Sync to cloud failed: {exc}")
            return False, f"Sync to cloud failed: {exc}"

    def sync_cloud_to_local(self, project_id, user_id):
        print(f"DEBUG SM: sync_cloud_to_local called project_id={project_id}, user_id={user_id}")
        if not clean_firebase_service.is_available():
            print("DEBUG SM: sync_cloud_to_local Cloud storage not available")
            return False, "Cloud storage not available"

        try:
            conn = self._connect()
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT cloud_project_id
                    FROM projects
                    WHERE id = ? AND user_id = ?
                """, (project_id, user_id))
                row = cursor.fetchone()
            finally:
                conn.close()

            if not row:
                print(f"DEBUG SM: sync_cloud_to_local Project {project_id} not found")
                return False, "Project not found"

            cloud_project_id = row[0]
            if not cloud_project_id:
                print(f"DEBUG SM: sync_cloud_to_local Project {project_id} not linked to a cloud project")
                return False, "This project is not linked to a cloud project"

            self._clear_local_project_data(project_id)
            self._copy_cloud_to_local(cloud_project_id, project_id, user_id)
            self._update_local_project_sync(project_id)
            print(f"DEBUG SM: sync_cloud_to_local successfully synced cloud project {cloud_project_id} to local {project_id}")
            return True, "Local project updated from cloud data"
        except Exception as exc:
            print(f"DEBUG SM: sync_cloud_to_local Sync from cloud failed: {exc}")
            return False, f"Sync from cloud failed: {exc}"

    def get_project_detail(self, user_id, identifier):
        """Fetch merged project entry for a given identifier (local or cloud id)"""
        print(f"DEBUG SM: get_project_detail called user_id={user_id}, identifier={identifier}")
        projects = self.get_projects(user_id)
        ident = str(identifier)
        for project in projects:
            if (project.get('local_id') and project['local_id'] == ident) or (
                project.get('cloud_id') and project['cloud_id'] == ident
            ):
                print(f"DEBUG SM: get_project_detail returning project {project['name']} via local_id/cloud_id match")
                return project
            if project.get('cloud_project_id') and project['cloud_project_id'] == ident:
                print(f"DEBUG SM: get_project_detail returning project {project['name']} via cloud_project_id match")
                return project
        print(f"DEBUG SM: get_project_detail no project found for identifier {identifier}")
        return None

# Global storage manager instance
storage_manager = StorageManager()