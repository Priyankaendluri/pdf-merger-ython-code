# merger.py

import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        print(f"🔗 Adding: {pdf}")
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"\n✅ Merged PDF saved to: {output_path}")

if __name__ == "__main__":
    # Change to your input folder path
    input_folder = "input"
    output_file = "output/merged.pdf"

    # Get list of PDFs in the input folder
    pdf_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.pdf')]
    pdf_files.sort()  # Optional: Sort alphabetically

    merge_pdfs(pdf_files, output_file)

