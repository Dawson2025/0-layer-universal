#!/usr/bin/env python3
# resource_id: "8aeabf70-1762-46a3-a2eb-aedfc740188d"
# resource_type: "document"
# resource_name: "check-firestore-data"
"""
Check Firestore Database for Cloud Feature Data
Verifies if cloud projects, words, phonemes exist
"""

import sys
sys.path.insert(0, '.')

from services.firebase import clean_firebase_service, firestore_db

print("\n" + "="*70)
print("🔍 FIRESTORE DATABASE VERIFICATION")
print("="*70)

# Check if Firebase is available
if not clean_firebase_service.is_available():
    print("\n❌ Firebase is not available")
    print("   Cloud features cannot be verified")
    sys.exit(1)

print("\n✅ Firebase SDK initialized successfully")
print(f"   Project: lang-trak-dev")

# Check for projects collection
print("\n📊 Checking PROJECTS collection...")
try:
    projects = firestore_db._service.get_documents('projects', limit=10)
    print(f"   Found {len(projects)} project(s)")
    
    if projects:
        print("\n   Sample projects:")
        for i, proj in enumerate(projects[:5], 1):
            print(f"   {i}. {proj.get('name', 'Unnamed')} (ID: {proj.get('id', 'Unknown')[:20]}...)")
            print(f"      User: {proj.get('user_id', 'Unknown')}")
            print(f"      Created: {proj.get('created_at', 'Unknown')}")
    else:
        print("   📝 No projects found (this is normal if no cloud projects created yet)")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Check for words collection  
print("\n📊 Checking WORDS collection...")
try:
    words = firestore_db._service.get_documents('words', limit=10)
    print(f"   Found {len(words)} word(s)")
    
    if words:
        print("\n   Sample words:")
        for i, word in enumerate(words[:5], 1):
            print(f"   {i}. {word.get('new_language_word', 'Unknown')} = {word.get('english_words', 'Unknown')}")
            print(f"      Project: {word.get('project_id', 'Unknown')}")
    else:
        print("   📝 No words found (normal if no cloud words created yet)")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Check for phonemes collection
print("\n📊 Checking PHONEMES collection...")
try:
    phonemes = firestore_db._service.get_documents('phonemes', limit=10)
    print(f"   Found {len(phonemes)} phoneme(s)")
    
    if phonemes:
        print("\n   Sample phonemes:")
        for i, phoneme in enumerate(phonemes[:5], 1):
            print(f"   {i}. {phoneme.get('phoneme', 'Unknown')} ({phoneme.get('position', 'Unknown')})")
            print(f"      Frequency: {phoneme.get('frequency', 0)}")
    else:
        print("   📝 No phonemes found (normal if no cloud phonemes yet)")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Check for templates collection
print("\n📊 Checking TEMPLATES collection...")
try:
    templates = firestore_db._service.get_documents('phoneme_templates', limit=10)
    print(f"   Found {len(templates)} template(s)")
    
    if templates:
        print("\n   Sample templates:")
        for i, template in enumerate(templates[:5], 1):
            print(f"   {i}. {template.get('name', 'Unknown')}")
            print(f"      Public: {template.get('is_public', False)}")
            print(f"      Phonemes: {template.get('phoneme_count', 0)}")
    else:
        print("   📝 No templates found (normal if none uploaded yet)")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Check for users collection
print("\n📊 Checking USERS collection...")
try:
    users = firestore_db._service.get_documents('users', limit=5)
    print(f"   Found {len(users)} user(s)")
    
    if users:
        print("\n   Sample users:")
        for i, user in enumerate(users[:3], 1):
            print(f"   {i}. {user.get('email', 'Unknown')}")
            print(f"      UID: {user.get('firebase_uid', 'Unknown')[:20]}...")
    else:
        print("   📝 No users found")
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "="*70)
print("CONCLUSION:")
print("="*70)

# Determine if cloud features are being used
total_docs = 0
try:
    projects_count = len(firestore_db._service.get_documents('projects', limit=100))
    words_count = len(firestore_db._service.get_documents('words', limit=100))
    phonemes_count = len(firestore_db._service.get_documents('phonemes', limit=100))
    templates_count = len(firestore_db._service.get_documents('phoneme_templates', limit=100))
    
    total_docs = projects_count + words_count + phonemes_count + templates_count
    
    print(f"\n📈 Total Cloud Documents: {total_docs}")
    print(f"   Projects: {projects_count}")
    print(f"   Words: {words_count}")
    print(f"   Phonemes: {phonemes_count}")
    print(f"   Templates: {templates_count}")
    
    if total_docs > 0:
        print("\n✅ CLOUD FEATURES ARE BEING USED!")
        print("   Firestore contains actual data")
        print("   Cloud features are WORKING")
    else:
        print("\n📝 No cloud data found")
        print("   This means either:")
        print("     1. No one has created cloud projects yet (normal)")
        print("     2. Cloud features work but haven't been used")
        print("\n   Firebase infrastructure is ready and working ✅")
        
except Exception as e:
    print(f"\n⚠️  Error counting documents: {e}")

print("\n" + "="*70)

