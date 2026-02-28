#!/usr/bin/env python3
"""Diagnostic script to identify video upload and conversion issues"""

import os
import subprocess
import tempfile
import sys

def check_ffmpeg_installation():
    """Check if FFmpeg is installed and accessible"""
    print("=== FFmpeg Installation Check ===")
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                               capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"✅ FFmpeg found: {version_line}")
            return True
        else:
            print("❌ FFmpeg command failed")
            print(f"Error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ FFmpeg not found in PATH")
        print("Please install FFmpeg:")
        print("  Windows: Download from https://ffmpeg.org/download.html")
        print("  Or use: winget install FFmpeg")
        return False
    except subprocess.TimeoutExpired:
        print("❌ FFmpeg command timed out")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_videos_directory():
    """Check videos directory permissions and accessibility"""
    print("\n=== Videos Directory Check ===")
    videos_dir = "videos"
    
    try:
        if not os.path.exists(videos_dir):
            print(f"📁 Creating videos directory: {videos_dir}")
            os.makedirs(videos_dir)
        
        if os.path.exists(videos_dir) and os.path.isdir(videos_dir):
            print(f"✅ Videos directory exists: {os.path.abspath(videos_dir)}")
            
            # Test write permissions
            test_file = os.path.join(videos_dir, "test_write.tmp")
            try:
                with open(test_file, 'w') as f:
                    f.write("test")
                os.remove(test_file)
                print("✅ Videos directory is writable")
                return True
            except Exception as e:
                print(f"❌ Videos directory not writable: {e}")
                return False
        else:
            print(f"❌ Videos directory not accessible")
            return False
            
    except Exception as e:
        print(f"❌ Error with videos directory: {e}")
        return False

def test_video_conversion():
    """Test video conversion with a dummy file"""
    print("\n=== Video Conversion Test ===")
    
    # Create a simple test video using FFmpeg (if available)
    with tempfile.TemporaryDirectory() as temp_dir:
        test_input = os.path.join(temp_dir, "test_input.mp4")
        test_output = os.path.join("videos", "diagnostic_test.mp4")
        
        try:
            # Create a simple test video (3 seconds, solid color)
            print("📹 Creating test video...")
            create_cmd = [
                'ffmpeg', '-f', 'lavfi', '-i', 'color=blue:size=320x240:rate=1:duration=3',
                '-y', test_input
            ]
            
            result = subprocess.run(create_cmd, capture_output=True, text=True, timeout=30)
            if result.returncode != 0:
                print(f"❌ Failed to create test video: {result.stderr}")
                return False
            
            print("✅ Test video created")
            
            # Now test conversion (same as your main.py function)
            print("🔄 Testing conversion...")
            convert_cmd = [
                'ffmpeg', '-i', test_input,
                '-c:v', 'libx264',
                '-c:a', 'aac',
                '-movflags', '+faststart',
                '-y', test_output
            ]
            
            result = subprocess.run(convert_cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print(f"✅ Video conversion successful: {test_output}")
                # Clean up test file
                if os.path.exists(test_output):
                    os.remove(test_output)
                    print("🧹 Cleaned up test file")
                return True
            else:
                print(f"❌ Video conversion failed")
                print(f"Command: {' '.join(convert_cmd)}")
                print(f"Error: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print("❌ Video conversion timed out")
            return False
        except Exception as e:
            print(f"❌ Video conversion error: {e}")
            return False

def check_common_video_formats():
    """Check if common video formats are supported"""
    print("\n=== Video Format Support Check ===")
    
    try:
        result = subprocess.run(['ffmpeg', '-formats'], 
                               capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            formats = result.stdout.lower()
            common_formats = ['mp4', 'avi', 'mov', 'mkv', 'webm', 'flv']
            supported = []
            for fmt in common_formats:
                if fmt in formats:
                    supported.append(fmt)
            
            print(f"✅ Supported formats: {', '.join(supported)}")
            return len(supported) > 0
        else:
            print("❌ Could not check format support")
            return False
    except Exception as e:
        print(f"❌ Error checking formats: {e}")
        return False

def check_existing_video_functionality():
    """Check if the main.py video functions exist and are accessible"""
    print("\n=== Main.py Video Functions Check ===")
    
    try:
        # Try to import main module
        sys.path.append('.')
        import main
        
        # Check if video functions exist
        functions_to_check = ['convert_video_to_mp4', 'handle_video_upload']
        missing_functions = []
        
        for func_name in functions_to_check:
            if hasattr(main, func_name):
                print(f"✅ Function {func_name} exists")
            else:
                print(f"❌ Function {func_name} missing")
                missing_functions.append(func_name)
        
        if not missing_functions:
            print("✅ All video functions are available")
            return True
        else:
            print(f"❌ Missing functions: {missing_functions}")
            return False
            
    except ImportError as e:
        print(f"❌ Could not import main.py: {e}")
        return False
    except Exception as e:
        print(f"❌ Error checking main.py functions: {e}")
        return False

def test_path_handling():
    """Test Windows path handling"""
    print("\n=== Path Handling Test ===")
    
    try:
        # Test various path formats
        test_paths = [
            "videos\\test.mp4",  # Windows backslash
            "videos/test.mp4",   # Unix forward slash
            os.path.join("videos", "test.mp4"),  # OS-specific
        ]
        
        for path in test_paths:
            normalized = os.path.normpath(path)
            absolute = os.path.abspath(path)
            print(f"✅ Path '{path}' → '{normalized}' → '{absolute}'")
        
        print("✅ Path handling working correctly")
        return True
        
    except Exception as e:
        print(f"❌ Path handling error: {e}")
        return False

def main():
    """Run all diagnostic checks"""
    print("🔍 Video Upload & Conversion Diagnostic Tool")
    print("=" * 50)
    
    issues_found = []
    
    # Check 1: Main.py functions
    if not check_existing_video_functionality():
        issues_found.append("Video functions missing or inaccessible in main.py")
    
    # Check 2: FFmpeg installation
    if not check_ffmpeg_installation():
        issues_found.append("FFmpeg not installed or not in PATH")
    
    # Check 3: Videos directory
    if not check_videos_directory():
        issues_found.append("Videos directory not accessible or writable")
    
    # Check 4: Path handling
    if not test_path_handling():
        issues_found.append("Path handling issues")
    
    # Check 5: Format support
    if not check_common_video_formats():
        issues_found.append("Video format support issues")
    
    # Check 6: Video conversion (only if FFmpeg works)
    if not any("FFmpeg" in str(issue) for issue in issues_found):
        if not test_video_conversion():
            issues_found.append("Video conversion failed")
    
    # Summary
    print("\n" + "=" * 50)
    print("🎯 DIAGNOSTIC SUMMARY")
    print("=" * 50)
    
    if not issues_found:
        print("✅ All checks passed! Video functionality should work.")
        print("\n💡 If you're still having issues, try:")
        print("   1. Make sure your input video file exists")
        print("   2. Use an absolute path to your video file")
        print("   3. Try a different video format (MP4, AVI, MOV)")
        print("   4. Check that the file isn't corrupted")
    else:
        print("❌ Issues found:")
        for i, issue in enumerate(issues_found, 1):
            print(f"   {i}. {issue}")
        
        print("\n🔧 SOLUTIONS:")
        if any("FFmpeg" in str(issue) for issue in issues_found):
            print("   📥 Install FFmpeg:")
            print("     • Windows: Download from https://ffmpeg.org/download.html")
            print("     • Or use: winget install FFmpeg")
            print("     • Or use: choco install ffmpeg")
            print("     • Add FFmpeg to your system PATH")
        
        if any("directory" in str(issue) for issue in issues_found):
            print("   📁 Fix directory issues:")
            print("     • Check folder permissions for the 'videos' directory")
            print("     • Try running as administrator")
            print("     • Make sure you have write access to the project folder")
        
        if any("conversion" in str(issue) for issue in issues_found):
            print("   🔄 Fix conversion issues:")
            print("     • Check if your input video file is valid")
            print("     • Try with a different video file")
            print("     • Check available disk space")
            print("     • Ensure the video file isn't in use by another program")
        
        if any("functions" in str(issue) for issue in issues_found):
            print("   🔧 Fix code issues:")
            print("     • Make sure main.py is in the current directory")
            print("     • Check that video functions are properly defined")
            print("     • Verify there are no syntax errors in main.py")

if __name__ == "__main__":
    main()
