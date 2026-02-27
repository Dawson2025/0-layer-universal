#!/usr/bin/env python3

"""
Manual Cloud Browser Tests

This script opens a browser and guides through manual testing of ALL cloud features.
It uses Playwright MCP for browser automation where possible, and provides
step-by-step instructions for manual verification.

Tests performed:
1. Google OAuth sign-in
2. Create cloud project
3. Add words & phonemes to cloud
4. Upload video to cloud storage
5. Create & upload phoneme template
6. Download & use cloud template  
7. Local → Cloud migration
8. Cloud → Local fork
9. TTS in cloud projects
10. Phoneme frequencies in cloud
11. Delete cloud resources
12. Verify all data in Firebase

Each test includes Firebase verification.

