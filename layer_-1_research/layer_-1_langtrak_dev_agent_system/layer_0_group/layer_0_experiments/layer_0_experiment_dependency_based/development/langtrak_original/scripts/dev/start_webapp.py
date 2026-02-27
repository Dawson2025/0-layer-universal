#!/usr/bin/env python3
"""
Startup script for the Phoneme Frequency Tracker Web Application
This script checks dependencies and provides instructions for running the web app.
"""

import sys
import os

def check_dependencies():
    """Check if required dependencies are available."""
    print("🔍 Checking dependencies...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required")
        return False
    else:
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} is available")
    
    # Check for required modules
    required_modules = ['sqlite3', 'os', 'json', 'subprocess', 'shutil', 'glob', 'platform', 'webbrowser']
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} is available")
        except ImportError:
            print(f"❌ {module} is not available")
            return False
    
    # Check if main.py is available
    if os.path.exists('main.py'):
        print("✅ main.py is available")
        try:
            import main
            print("✅ main.py imports successfully")
        except Exception as e:
            print(f"❌ Error importing main.py: {e}")
            return False
    else:
        print("❌ main.py not found")
        return False
    
    # Check for Flask
    try:
        import flask
        print(f"✅ Flask {flask.__version__} is available")
        return True
    except ImportError:
        print("⚠️  Flask is not installed")
        return False

def show_installation_instructions():
    """Show instructions for installing Flask."""
    print("\n📦 Flask Installation Instructions:")
    print("=" * 50)
    print("Option 1 - Using virtual environment (recommended):")
    print("  python3 -m venv venv")
    print("  source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
    print("  pip install flask")
    print("  python app.py")
    print()
    print("Option 2 - System-wide installation:")
    print("  pip install flask")
    print("  python app.py")
    print()
    print("Option 3 - Using requirements.txt:")
    print("  pip install -r requirements.txt")
    print("  python app.py")

def show_features():
    """Show the implemented features."""
    print("\n🚀 Implemented Features:")
    print("=" * 50)
    print("📱 Web Interface Features:")
    print("  ✅ Modern responsive design with dark theme")
    print("  ✅ Mobile-first approach with touch-friendly UI")
    print("  ✅ Real-time updates and dynamic content loading")
    print("  ✅ Search and filtering capabilities")
    print()
    print("🔤 Phoneme Management:")
    print("  ✅ Flat view - Simple list with search")
    print("  ✅ Nested view - Hierarchical organization")
    print("  ✅ Full hierarchy - Complete structure with frequencies")
    print("  ✅ Admin panel - Add, edit, delete phonemes")
    print()
    print("📚 Word Management:")
    print("  ✅ Table-based word creation with phoneme selection")
    print("  ✅ Real-time IPA building from selected phonemes")
    print("  ✅ Word lookup with multi-criteria search")
    print("  ✅ Word editing with structured phoneme data")
    print("  ✅ Word deletion with frequency updates")
    print("  ✅ Comprehensive word browser with statistics")
    print()
    print("🎯 User Stories Implemented:")
    print("  ✅ Table-based word creation with hierarchy display")
    print("  ✅ Phoneme frequency visualization and management")
    print("  ✅ Advanced search and filtering system")
    print("  ✅ Complete admin control panel")
    print("  ✅ Responsive design for all device sizes")

def show_terminal_functions_mapped():
    """Show how terminal functions were mapped to web features."""
    print("\n🔄 Terminal Functions → Web Features Mapping:")
    print("=" * 60)
    
    mappings = [
        ("display_flat()", "GET /phonemes/flat - Flat phoneme view"),
        ("display_nested_phonemes()", "GET /phonemes/nested - Nested hierarchy"),
        ("display_full()", "GET /phonemes/full - Full hierarchy view"),
        ("create_word_table_based()", "GET /words/create/table-based - Word creation"),
        ("display_words()", "GET /words/display - All words browser"),
        ("lookup_word()", "GET /words/lookup - Word search interface"),
        ("edit_existing_word()", "GET /words/edit/<id> - Word editing"),
        ("delete_word_by_lookup()", "DELETE /api/delete-word/<id> - Word deletion"),
        ("admin_menu()", "GET /admin/phonemes - Admin panel"),
        ("add_new_phoneme()", "POST /api/admin/add-phoneme - Add phoneme"),
        ("increase_frequency()", "POST /api/admin/update-phoneme-frequency"),
        ("decrease_frequency()", "POST /api/admin/update-phoneme-frequency"),
        ("delete_phoneme()", "DELETE /api/admin/delete-phoneme/<id>"),
        ("reset_database()", "POST /api/admin/reset-database"),
    ]
    
    for terminal_func, web_endpoint in mappings:
        print(f"  {terminal_func:<25} → {web_endpoint}")

def main():
    """Main startup function."""
    print("🎯 Phoneme Frequency Tracker - Web Application")
    print("=" * 60)
    print("A comprehensive web interface implementing all terminal functions")
    print("as modern web features with responsive design and real-time updates.")
    print()
    
    # Check dependencies
    has_flask = check_dependencies()
    
    if has_flask:
        print("\n🎉 All dependencies are available!")
        print("To start the web application, run:")
        print("  python3 app.py")
        print("\nThen open your browser to: http://localhost:5000")
        
        # Try to start the app
        try:
            print("\n🚀 Starting web application...")
            import app
            # The app.run() call is at the bottom of app.py, so importing will start it
        except ImportError as e:
            print(f"❌ Error starting web app: {e}")
            show_installation_instructions()
    else:
        show_installation_instructions()
    
    # Show features regardless
    show_features()
    show_terminal_functions_mapped()
    
    print("\n📖 For detailed information, see WEB_APP_README.md")
    print("🎯 All user stories from terminal functions have been implemented!")

if __name__ == "__main__":
    main()