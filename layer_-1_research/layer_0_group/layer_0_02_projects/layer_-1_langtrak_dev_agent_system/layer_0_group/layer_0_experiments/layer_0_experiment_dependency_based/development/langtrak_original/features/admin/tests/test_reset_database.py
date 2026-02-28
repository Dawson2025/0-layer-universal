#!/usr/bin/env python3
"""
Test the enhanced reset_database function with warnings and confirmations
"""
import sys
import os
from unittest.mock import patch
from services.reset.database import ResetResult
import main

def test_reset_database_cancelled_first_prompt():
    """Test reset cancelled at first confirmation"""
    print("Testing reset cancellation at first prompt...")
    
    with patch('builtins.input', side_effect=["no", ""]):  # Say no, then press enter
        with patch('builtins.print') as mock_print:
            main.reset_database()
            
            # Check that cancellation message was shown
            print_calls = [str(call) for call in mock_print.call_args_list]
            print_text = ' '.join(print_calls)
            assert "Database reset cancelled" in print_text, "Should show cancellation message"
    
    print("✓ First prompt cancellation test passed")

def test_reset_database_cancelled_verification():
    """Test reset cancelled at verification step"""
    print("Testing reset cancellation at verification step...")
    
    with patch('os.path.exists', return_value=True):
        with patch('main.get_database_snapshot', return_value={'phonemes': 15, 'words': 7}):
            with patch('builtins.input', side_effect=["yes", "WRONG TEXT", ""]):  # Yes, wrong text, enter
                with patch('builtins.print') as mock_print:
                    main.reset_database()

                    # Check that verification failed message was shown
                    print_calls = [str(call) for call in mock_print.call_args_list]
                    print_text = ' '.join(print_calls)
                    assert "Verification failed" in print_text, "Should show verification failed message"
    
    print("✓ Verification cancellation test passed")

def test_reset_database_warnings_displayed():
    """Test that proper warnings are displayed"""
    print("Testing warning display...")
    
    with patch('builtins.input', side_effect=["no", ""]):  # Cancel at first prompt
        with patch('builtins.print') as mock_print:
            main.reset_database()
            
            # Check that warnings were displayed
            print_calls = [str(call) for call in mock_print.call_args_list]
            print_text = ' '.join(print_calls)
            
            assert "WARNING: DATABASE RESET" in print_text, "Should show warning header"
            assert "PERMANENTLY DELETE" in print_text, "Should warn about permanent deletion"
            assert "All phonemes and their frequencies" in print_text, "Should mention phonemes"
            assert "All words in your language database" in print_text, "Should mention words"
            assert "Everything will be lost forever" in print_text, "Should emphasize permanence"
    
    print("✓ Warning display test passed")

def test_reset_database_successful_flow():
    """Test successful reset with proper confirmations"""
    print("Testing successful reset flow...")
    
    # Mock the database operations
    with patch('os.path.exists', return_value=True):
        with patch('main.get_database_snapshot', return_value={'phonemes': 10, 'words': 5}):
            with patch('main.perform_database_reset', return_value=ResetResult(templates_preserved=2, words_deleted=5, phonemes_deleted=10)) as mock_reset:
                with patch('builtins.input', side_effect=["yes", "DELETE EVERYTHING", ""]):
                    with patch('builtins.print') as mock_print:
                        main.reset_database()

                        print_calls = [str(call) for call in mock_print.call_args_list]
                        print_text = ' '.join(print_calls)
                        assert "Database successfully reset" in print_text, "Should show success message"
                        assert "Preserved 2 phoneme templates" in print_text, "Should mention templates preserved"

                        mock_reset.assert_called_once_with(main.DB_NAME, insert_sample_data=main.insert_sample_data)
    
    print("✓ Successful reset flow test passed")

def test_database_content_display():
    """Test that database content counts are displayed"""
    print("Testing database content display...")
    
    # Mock database with content - need to say 'yes' first to reach the content display
    with patch('os.path.exists', return_value=True):
        with patch('main.get_database_snapshot', return_value={'phonemes': 25, 'words': 12}):
            # Say yes to first prompt, but fail verification to avoid actual reset
            with patch('builtins.input', side_effect=["yes", "WRONG VERIFICATION", ""]):
                with patch('builtins.print') as mock_print:
                    main.reset_database()

                    print_calls = [str(call) for call in mock_print.call_args_list]
                    print_text = ' '.join(print_calls)

                    assert "25 phonemes" in print_text, f"Should show phoneme count in: {print_text[:200]}..."
                    assert "12 words" in print_text, f"Should show word count in: {print_text[:200]}..."
    
    print("✓ Database content display test passed")

def display_reset_process_flow():
    """Display the reset process flow for documentation"""
    print("\n=== RESET DATABASE PROCESS FLOW ===")
    print("1. Display dramatic warning with emoji and formatting")
    print("2. List all data types that will be deleted")
    print("3. First confirmation: 'Are you ABSOLUTELY SURE?' (yes/no)")
    print("4. If cancelled → Return to menu")
    print("5. Show current database contents (phoneme/word counts)")
    print("6. Second confirmation: Type 'DELETE EVERYTHING' exactly")
    print("7. If verification fails → Return to menu")
    print("8. Perform database deletion and recreation")
    print("9. Display success message")
    print("10. Return to menu")
    
    print("\n=== SAFETY FEATURES ===")
    print("• Two-step confirmation process")
    print("• Must type exact phrase 'DELETE EVERYTHING'")
    print("• Shows current data counts before deletion")
    print("• Clear warnings about permanent data loss")
    print("• Multiple cancellation points")
    print("• Error handling for database operations")

if __name__ == "__main__":
    print("Testing Enhanced Reset Database Function\n")
    
    try:
        test_reset_database_warnings_displayed()
        test_reset_database_cancelled_first_prompt()
        test_reset_database_cancelled_verification()
        test_database_content_display()
        test_reset_database_successful_flow()
        display_reset_process_flow()
        
        print("\n🎉 ALL RESET DATABASE TESTS PASSED!")
        print("✅ Enhanced safety features implemented:")
        print("   • Dramatic warning messages with emoji")
        print("   • Two-step confirmation process")
        print("   • Current data count display")
        print("   • Exact phrase verification ('DELETE EVERYTHING')")
        print("   • Multiple cancellation opportunities")
        print("   • Clear success/error messaging")
        print("   • Proper error handling")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)
