#!/usr/bin/env python3
"""
Analyze iMessage conversation PDFs and categorize them
based on the life optimization framework
"""

import os
import sys
from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

# Life optimization categories based on your framework
CATEGORIES = {
    "Physical and Mental Health": [
        "health", "fitness", "exercise", "diet", "nutrition", "mental", "therapy",
        "doctor", "medical", "wellness", "sleep", "stress", "anxiety", "depression"
    ],
    "Social Connections and Relationships": [
        "friend", "relationship", "family", "social", "connect", "love", "dating",
        "marriage", "partner", "wife", "husband", "girlfriend", "boyfriend"
    ],
    "Meaningful Work and Financial Stability": [
        "work", "job", "career", "business", "money", "finance", "salary", "income",
        "investment", "budget", "debt", "savings", "stock", "401k", "retirement"
    ],
    "Personal Growth and Lifelong Learning": [
        "learn", "education", "study", "course", "skill", "development", "growth",
        "book", "reading", "knowledge", "training", "improve", "practice"
    ],
    "Leisure, Play, and Appreciation of Life": [
        "fun", "hobby", "game", "vacation", "travel", "entertainment", "music",
        "movie", "art", "play", "enjoy", "relax", "adventure"
    ],
    "Meaning, Purpose, and Spirituality": [
        "purpose", "meaning", "spiritual", "religion", "faith", "meditation",
        "mindfulness", "values", "philosophy", "belief", "god", "prayer"
    ]
}

def extract_sample_text(pdf_path, num_samples=5, dpi=150):
    """Extract text from a sample of pages using OCR"""
    print(f"\n{'='*80}")
    print(f"Analyzing: {os.path.basename(pdf_path)}")
    print(f"{'='*80}\n")
    
    try:
        # Convert first page to images
        print("Converting PDF to images (this may take a minute)...")
        images = convert_from_path(pdf_path, dpi=dpi, first_page=1, last_page=1)
        
        if not images:
            print("ERROR: No images extracted from PDF")
            return ""
        
        # Since this is one long screenshot page, we'll process it in sections
        print(f"Extracted {len(images)} page(s)")
        
        all_text = []
        for i, image in enumerate(images):
            print(f"\nProcessing image {i+1}/{len(images)}...")
            
            # Crop into sections if the image is very tall
            width, height = image.size
            print(f"Image size: {width}x{height}")
            
            # Process top, middle, and bottom sections
            sections = []
            if height > 3000:  # Very tall image
                sections = [
                    ("top", image.crop((0, 0, width, 1000))),
                    ("middle", image.crop((0, height//2 - 500, width, height//2 + 500))),
                    ("bottom", image.crop((0, max(0, height - 1000), width, height)))
                ]
            else:
                sections = [("full", image)]
            
            for section_name, section_img in sections:
                print(f"  OCR on {section_name} section...")
                text = pytesseract.image_to_string(section_img)
                if text.strip():
                    all_text.append(f"\n=== {section_name.upper()} SECTION ===\n{text}")
        
        combined_text = "\n".join(all_text)
        print(f"\n✓ Extracted {len(combined_text)} characters of text")
        return combined_text
    
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        return ""

def categorize_text(text):
    """Categorize text based on keyword matching"""
    text_lower = text.lower()
    category_scores = {}
    
    for category, keywords in CATEGORIES.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        category_scores[category] = score
    
    # Sort by score
    sorted_categories = sorted(category_scores.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_categories

def analyze_pdf(pdf_path):
    """Main analysis function"""
    # Extract text sample
    text = extract_sample_text(pdf_path)
    
    if not text:
        print("\n⚠️  Could not extract text from PDF")
        return None
    
    # Save extracted text
    text_file = pdf_path.replace('.PDF', '_extracted.txt')
    with open(text_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"\n✓ Saved extracted text to: {text_file}")
    
    # Show preview
    print(f"\n{'='*80}")
    print("TEXT PREVIEW (first 1000 chars):")
    print(f"{'='*80}")
    print(text[:1000])
    print(f"{'='*80}\n")
    
    # Categorize
    categories = categorize_text(text)
    
    print("\n📊 CATEGORY ANALYSIS:")
    print("="*80)
    for category, score in categories:
        if score > 0:
            print(f"  {category}: {score} relevant keywords")
    
    # Determine primary category
    if categories[0][1] > 0:
        primary = categories[0][0]
        print(f"\n🎯 PRIMARY CATEGORY: {primary}")
        print(f"\n📁 RECOMMENDED FOLDER: ACCOUNTS/{primary}/")
    else:
        print(f"\n⚠️  No strong category match found")
        print(f"\n📁 RECOMMENDED FOLDER: ACCOUNTS/misc/")
    
    return categories

def main():
    """Process both PDFs"""
    pdf_dir = Path("info")
    pdfs = list(pdf_dir.glob("*.PDF"))
    
    if not pdfs:
        print("ERROR: No PDF files found in info/")
        sys.exit(1)
    
    print(f"\n🔍 Found {len(pdfs)} PDF file(s) to analyze\n")
    
    results = {}
    for pdf in pdfs:
        result = analyze_pdf(str(pdf))
        results[pdf.name] = result
        print("\n" + "="*80 + "\n")
    
    # Summary
    print("\n" + "="*80)
    print("📋 SUMMARY")
    print("="*80 + "\n")
    
    for pdf_name, categories in results.items():
        if categories and categories[0][1] > 0:
            primary = categories[0][0]
            print(f"✓ {pdf_name}")
            print(f"  → ACCOUNTS/{primary}/")
        else:
            print(f"? {pdf_name}")
            print(f"  → ACCOUNTS/misc/ (no clear category)")
        print()

if __name__ == "__main__":
    main()

