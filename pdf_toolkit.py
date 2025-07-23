import os
import sys
from PyPDF2 import PdfReader, PdfWriter
from tkinter import filedialog

def merge_pdfs(file_list, output_name="merged.pdf"):
    writer = PdfWriter()
    for file in file_list:
        reader = PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_name, "wb") as f:
        writer.write(f)
    print(f"✅ Merged PDF saved as {output_name}")

def split_pdf(file_path):
    reader = PdfReader(file_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_file = f"page_{i+1}.pdf"
        with open(output_file, "wb") as f:
            writer.write(f)
        print(f"📄 Saved: {output_file}")

def extract_text(file_path):
    reader = PdfReader(file_path)
    print("📄 Extracted Text:")
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"\n--- Page {i+1} ---\n{text}")

def main():
    print("🧰 PDF Toolkit Options:")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Extract Text")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        files = filedialog.askopenfilenames(title="Select PDF files to merge")
        merge_pdfs(files)
    elif choice == "2":
        file = filedialog.askopenfilename(title="Select PDF to split")
        split_pdf(file)
    elif choice == "3":
        file = filedialog.askopenfilename(title="Select PDF to extract text from")
        extract_text(file)
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
