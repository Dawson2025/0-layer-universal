#!/usr/bin/env python3

"""
Cleanup Test Data from Firebase

This script removes test data from Firebase that was created during E2E testing.
It searches for documents with specific markers in their names and deletes them.

Usage:
    python3 scripts/cleanup-test-data.py --marker "E2E_TEST_123456"
    python3 scripts/cleanup-test-data.py --all-test-data
    python3 scripts/cleanup-test-data.py --dry-run --marker "Manual_Test"
"""

import sys
import os
import argparse
from datetime import datetime, timedelta

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.firebase import clean_firebase_service, firestore_db

def cleanup_test_data(marker=None, all_test_data=False, dry_run=False, days_old=None):
    """
    Clean up test data from Firebase.
    
    Args:
        marker: String marker to identify test data (e.g., "E2E_TEST_123")
        all_test_data: If True, remove all documents with test markers
        dry_run: If True, only report what would be deleted
        days_old: Only delete test data older than X days
    """
    
    if not clean_firebase_service.is_available():
        print("❌ Firebase not available")
        return False
    
    print("\n" + "="*70)
    print("🧹 FIREBASE TEST DATA CLEANUP")
    print("="*70)
    print(f"\nMode: {'DRY RUN' if dry_run else 'LIVE DELETE'}")
    
    if marker:
        print(f"Marker: {marker}")
    elif all_test_data:
        print("Target: ALL test data")
    
    if days_old:
        print(f"Age filter: Older than {days_old} days")
    
    print("\n" + "-"*70)
    
    deleted_counts = {
        'projects': 0,
        'words': 0,
        'templates': 0,
        'phonemes': 0
    }
    
    # Common test markers
    test_markers = [
        'E2E_TEST_',
        'Manual_Test_',
        'Cloud_E2E_',
        'Test_Project_',
        'AUTOMATION_',
        '__test__',
        'pytest_'
    ]
    
    def should_delete(doc):
        """Determine if a document should be deleted."""
        name = doc.get('name', '')
        created_at = doc.get('created_at')
        
        # Check marker match
        if marker and marker not in name:
            return False
        
        if not marker and all_test_data:
            # Check if name contains any test marker
            if not any(tm in name for tm in test_markers):
                return False
        
        # Check age if specified
        if days_old and created_at:
            try:
                if hasattr(created_at, 'date'):
                    doc_date = created_at.date()
                else:
                    from dateutil import parser
                    doc_date = parser.parse(str(created_at)).date()
                
                age = (datetime.now().date() - doc_date).days
                if age < days_old:
                    return False
            except:
                pass
        
        return True
    
    # Cleanup projects
    print("\n📂 Scanning projects...")
    try:
        projects = firestore_db._service.get_documents('projects', limit=1000)
        projects_to_delete = [p for p in projects if should_delete(p)]
        
        print(f"   Found {len(projects_to_delete)} project(s) to delete")
        
        for proj in projects_to_delete:
            proj_id = proj.get('id')
            proj_name = proj.get('name', 'Unknown')
            
            if dry_run:
                print(f"   [DRY RUN] Would delete: {proj_name} (ID: {proj_id})")
            else:
                try:
                    firestore_db._service.delete_document('projects', proj_id)
                    print(f"   ✅ Deleted: {proj_name}")
                    deleted_counts['projects'] += 1
                except Exception as e:
                    print(f"   ❌ Error deleting {proj_name}: {e}")
            
    except Exception as e:
        print(f"   ❌ Error scanning projects: {e}")
    
    # Cleanup words (orphaned or from deleted projects)
    print("\n📝 Scanning words...")
    try:
        words = firestore_db._service.get_documents('words', limit=1000)
        project_ids = [p.get('id') for p in projects_to_delete]
        
        # Words belonging to deleted projects OR with test markers
        words_to_delete = [
            w for w in words 
            if w.get('project_id') in project_ids or should_delete(w)
        ]
        
        print(f"   Found {len(words_to_delete)} word(s) to delete")
        
        for word in words_to_delete:
            word_id = word.get('id')
            word_text = word.get('english_word', 'Unknown')
            
            if dry_run:
                print(f"   [DRY RUN] Would delete: {word_text} (ID: {word_id})")
            else:
                try:
                    firestore_db._service.delete_document('words', word_id)
                    print(f"   ✅ Deleted: {word_text}")
                    deleted_counts['words'] += 1
                except Exception as e:
                    print(f"   ❌ Error deleting {word_text}: {e}")
            
    except Exception as e:
        print(f"   ❌ Error scanning words: {e}")
    
    # Cleanup templates
    print("\n📋 Scanning templates...")
    try:
        templates = firestore_db._service.get_documents('templates', limit=1000)
        templates_to_delete = [t for t in templates if should_delete(t)]
        
        print(f"   Found {len(templates_to_delete)} template(s) to delete")
        
        for template in templates_to_delete:
            template_id = template.get('id')
            template_name = template.get('name', 'Unknown')
            
            if dry_run:
                print(f"   [DRY RUN] Would delete: {template_name} (ID: {template_id})")
            else:
                try:
                    firestore_db._service.delete_document('templates', template_id)
                    print(f"   ✅ Deleted: {template_name}")
                    deleted_counts['templates'] += 1
                except Exception as e:
                    print(f"   ❌ Error deleting {template_name}: {e}")
            
    except Exception as e:
        print(f"   ❌ Error scanning templates: {e}")
    
    # Cleanup phonemes (orphaned)
    print("\n🔤 Scanning phonemes...")
    try:
        phonemes = firestore_db._service.get_documents('phonemes', limit=1000)
        phonemes_to_delete = [
            ph for ph in phonemes 
            if ph.get('project_id') in project_ids
        ]
        
        print(f"   Found {len(phonemes_to_delete)} phoneme(s) to delete")
        
        for phoneme in phonemes_to_delete:
            phoneme_id = phoneme.get('id')
            
            if dry_run:
                print(f"   [DRY RUN] Would delete phoneme ID: {phoneme_id}")
            else:
                try:
                    firestore_db._service.delete_document('phonemes', phoneme_id)
                    deleted_counts['phonemes'] += 1
                except Exception as e:
                    print(f"   ❌ Error deleting phoneme: {e}")
        
        if not dry_run and phonemes_to_delete:
            print(f"   ✅ Deleted {deleted_counts['phonemes']} phoneme(s)")
            
    except Exception as e:
        print(f"   ❌ Error scanning phonemes: {e}")
    
    # Summary
    print("\n" + "="*70)
    print("CLEANUP SUMMARY")
    print("="*70)
    
    for collection, count in deleted_counts.items():
        status = "[WOULD DELETE]" if dry_run else "✅"
        print(f"{status} {collection.capitalize()}: {count}")
    
    total = sum(deleted_counts.values())
    print(f"\n{'Would delete' if dry_run else 'Deleted'} {total} document(s) total")
    
    if dry_run:
        print("\n💡 Run without --dry-run to actually delete these documents")
    
    print("="*70 + "\n")
    
    return True

def main():
    parser = argparse.ArgumentParser(
        description='Cleanup test data from Firebase',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run for specific marker
  python3 scripts/cleanup-test-data.py --marker "E2E_TEST_123" --dry-run
  
  # Delete data with specific marker
  python3 scripts/cleanup-test-data.py --marker "Manual_Test_Cloud"
  
  # Delete all test data (be careful!)
  python3 scripts/cleanup-test-data.py --all-test-data
  
  # Delete test data older than 7 days
  python3 scripts/cleanup-test-data.py --all-test-data --days-old 7
        """
    )
    
    parser.add_argument(
        '--marker',
        type=str,
        help='Specific marker to identify test data (e.g., "E2E_TEST_123")'
    )
    
    parser.add_argument(
        '--all-test-data',
        action='store_true',
        help='Delete ALL test data (use with caution!)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be deleted without actually deleting'
    )
    
    parser.add_argument(
        '--days-old',
        type=int,
        help='Only delete test data older than X days'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.marker and not args.all_test_data:
        parser.error("Must specify either --marker or --all-test-data")
    
    if args.all_test_data and not args.dry_run:
        print("\n⚠️  WARNING: You are about to delete ALL test data from Firebase!")
        print("This action cannot be undone.")
        response = input("\nType 'DELETE ALL TEST DATA' to confirm: ")
        
        if response != 'DELETE ALL TEST DATA':
            print("❌ Cancelled")
            return
    
    # Run cleanup
    cleanup_test_data(
        marker=args.marker,
        all_test_data=args.all_test_data,
        dry_run=args.dry_run,
        days_old=args.days_old
    )

if __name__ == '__main__':
    main()

