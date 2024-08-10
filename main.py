import os
import pikepdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import argparse

def add_page_numbers(input_pdf, output_pdf, start_number=1, skip_first_pages=3):
    pdf_writer = pikepdf.Pdf.new()
    pdf_reader = pikepdf.Pdf.open(input_pdf)
    
    for page_num, page in enumerate(pdf_reader.pages):
        if page_num < skip_first_pages:
            pdf_writer.pages.append(page)
            continue
        
        # Create a temporary PDF with page number
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # Set a smaller font size
        can.setFont("Helvetica", 8)
        
        # Calculate the page number to display
        display_number = start_number + page_num - skip_first_pages
        can.drawString(500, 20, str(display_number + 2))  # Adjust coordinates and start number
        can.save()
        
        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = pikepdf.Pdf.open(packet)
        
        # Merge the page number PDF with the original page
        new_page = new_pdf.pages[0]
        page.merge_page(new_page)
        pdf_writer.pages.append(page)
    
    # Write out the final PDF with page numbers
    pdf_writer.save(output_pdf)
    print(f'PDF with page numbers saved as {output_pdf}')

def merge_pdfs(output_pdf, pdf_files):
    pdf_writer = pikepdf.Pdf.new()
    
    for pdf_file in pdf_files:
        if not os.path.isfile(pdf_file):
            print(f"File not found: {pdf_file}")
            continue
        
        try:
            pdf_reader = pikepdf.Pdf.open(pdf_file)
            print(f"Adding {pdf_file} with {len(pdf_reader.pages)} pages")
            for page in pdf_reader.pages:
                pdf_writer.pages.append(page)
        except pikepdf.PdfError as e:
            print(f"Error reading {pdf_file}: {e}")
        except Exception as e:
            print(f"Unexpected error with {pdf_file}: {e}")
    
    # Save the merged PDF before adding page numbers
    temp_output_pdf = 'temp_merged_notes.pdf'
    try:
        pdf_writer.save(temp_output_pdf)
        print(f'Merged PDF saved as {temp_output_pdf}')
    except Exception as e:
        print(f"Error saving merged PDF: {e}")
        return
    
    # Add page numbers to the merged PDF
    add_page_numbers(temp_output_pdf, output_pdf, start_number=1, skip_first_pages=3)
    
    # Optionally, remove the temporary file
    if os.path.isfile(temp_output_pdf):
        os.remove(temp_output_pdf)

def main():
    parser = argparse.ArgumentParser(description="Merge PDFs and add page numbers.")
    parser.add_argument('output_pdf', type=str, help="Output PDF file name.")
    parser.add_argument('pdf_files', type=str, nargs='+', help="List of PDF files to merge in order.")
    
    args = parser.parse_args()
    
    output_pdf = args.output_pdf
    pdf_files = args.pdf_files
    
    # Check if all files exist
    missing_files = [file for file in pdf_files if not os.path.isfile(file)]
    if missing_files:
        print(f"Missing files: {', '.join(missing_files)}")
        return
    
    # Merge the PDFs
    merge_pdfs(output_pdf, pdf_files)

if __name__ == "__main__":
    main()
