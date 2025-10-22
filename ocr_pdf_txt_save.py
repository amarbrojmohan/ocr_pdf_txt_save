# Code based on ChatGPT response
# This code is a debugged working version on Windows

from pdf2image import convert_from_path
import pytesseract

# On Windows, path set to tesseract.exe manually
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set the path to your PDF
pdf_path = "OCR_test.pdf"

# Convert pages 1–8 into images
images = convert_from_path(pdf_path, first_page=1, last_page=8, poppler_path=r"H:\AMR\PYTHON\poppler-25.07.0\Library\bin")

# Prepare output file
output_file = "OCR_test.txt"

# OCR each page and write to file
with open(output_file, "w", encoding="utf-8") as f:
    for i, img in enumerate(images, start=1):
        text = pytesseract.image_to_string(img, lang='hin+eng').strip()
        f.write(f"\n--- Page {i} ---\n{text}\n")
        print(f"✅ Extracted page {i}")

print(f"\n OCR completed! Extracted text saved to: {output_file}")
