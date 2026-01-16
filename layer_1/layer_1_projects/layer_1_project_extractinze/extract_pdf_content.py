#!/usr/bin/env python3
"""
Extract text content from image-based PDF files using OCR
"""

import sys
import os

try:
    from pdf2image import convert_from_path
    from PIL import Image
    import pytesseract
except ImportError:
    print("Installing required packages...")
    os.system("pip install pdf2image pillow pytesseract --break-system-packages")
    from pdf2image import convert_from_path
    from PIL import Image
    import pytesseract

def extract_text_from_pdf(pdf_path, max_pages=10):
    """Extract text from image-based PDF using OCR"""
    print(f"Processing: {pdf_path}")
    print("Converting PDF to images...")
    
    try:
        # Convert PDF to images (first few pages only for analysis)
        images = convert_from_path(pdf_path, first_page=1, last_page=max_pages)
        
        print(f"Extracted {len(images)} page(s)")
        
        all_text = []
        for i, image in enumerate(images):
            print(f"OCR on page {i+1}...")
            text = pytesseract.image_to_string(image)
            all_text.append(text)
        
        return "\n\n=== PAGE BREAK ===\n\n".join(all_text)
    
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract_pdf_content.py <pdf_file>")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    
    text = extract_text_from_pdf(pdf_file, max_pages)
    
    if text:
        output_file = pdf_file.replace('.PDF', '.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"\nText saved to: {output_file}")
        print("\n" + "="*80)
        print("PREVIEW (first 2000 characters):")
        print("="*80)
        print(text[:2000])
    else:
        print("Failed to extract text")

