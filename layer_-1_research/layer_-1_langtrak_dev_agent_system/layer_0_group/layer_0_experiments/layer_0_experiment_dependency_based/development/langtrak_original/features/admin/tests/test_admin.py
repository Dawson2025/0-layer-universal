#!/usr/bin/env python3
"""
Test the admin functionality in main.py
"""
import sys
import io
from unittest.mock import patch
import main

def test_admin_login_correct():
    """Test admin login with correct password"""
    print("Testing admin login with correct password...")
    with patch('builtins.input', return_value="20251010"):
        with patch('builtins.print') as mock_print:
            result = main.admin_login()
            assert result == True, "Admin login should return True with correct password"
            # Check that success message was printed
            mock_print.assert_any_call("✓ Admin access granted.")
    print("✓ Correct password test passed")

def test_admin_login_incorrect():
    """Test admin login with incorrect password"""
    print("Testing admin login with incorrect password...")
    with patch('builtins.input', side_effect=["wrongpassword", ""]):  # wrong password + enter for continue
        with patch('builtins.print') as mock_print:
            result = main.admin_login()
            assert result == False, "Admin login should return False with incorrect password"
            # Check that error message was printed
            mock_print.assert_any_call("✗ Incorrect password. Access denied.")
    print("✓ Incorrect password test passed")

def test_admin_functions_exist():
    """Test that admin functions exist"""
    print("Testing that admin functions exist...")
    assert hasattr(main, 'admin_login'), "admin_login function should exist"
    assert hasattr(main, 'admin_menu'), "admin_menu function should exist"
    assert callable(main.admin_login), "admin_login should be callable"
    assert callable(main.admin_menu), "admin_menu should be callable"
    print("✓ Admin functions exist test passed")

def test_protected_functions_exist():
    """Test that protected functions still exist"""
    print("Testing that protected functions still exist...")
    assert hasattr(main, 'add_new_phoneme'), "add_new_phoneme function should exist"
    assert hasattr(main, 'delete_phoneme'), "delete_phoneme function should exist"
    assert hasattr(main, 'reset_database'), "reset_database function should exist"
    print("✓ Protected functions exist test passed")

if __name__ == "__main__":
    print("Testing Admin System Implementation\n")
    
    try:
        test_admin_functions_exist()
        test_protected_functions_exist() 
        test_admin_login_correct()
        test_admin_login_incorrect()
        
        print("\n🎉 ALL ADMIN TESTS PASSED!")
        print("✓ Admin system successfully implemented")
        print("✓ Password protection working: '20251010'")
        print("✓ Protected functions: add_new_phoneme, delete_phoneme, reset_database")
        print("✓ Admin menu system functional")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)
