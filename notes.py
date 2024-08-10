import PyPDF2
import os
import logging
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from io import BytesIO

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_page_numbers(input_pdf, output_pdf, start_number=1, skip_first_pages=3):
    pdf_writer = PyPDF2.PdfWriter()
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        
        if page_num < skip_first_pages:
            # Directly add the first few pages without numbering
            pdf_writer.add_page(page)
            continue
        
        # Create a temporary PDF with page number
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # Set a smaller font size
        can.setFont("Helvetica", 10)
        
        # Calculate the page number to display
        display_number = start_number + page_num - skip_first_pages
        can.drawString(460, 10, f'PAGE {str(display_number + 2)}')  # Adjust coordinates and start number
        can.save()
        
        # Move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PyPDF2.PdfReader(packet)
        
        # Merge the page number PDF with the original page
        page.merge_page(new_pdf.pages[0])
        pdf_writer.add_page(page)
    
    # Write out the final PDF with page numbers
    with open(output_pdf, 'wb') as out_file:
        pdf_writer.write(out_file)
    logging.info(f'PDF with page numbers saved as {output_pdf}')

def merge_pdfs(output_pdf, pdf_files):
    pdf_writer = PyPDF2.PdfWriter()
    
    for pdf_file in pdf_files:
        if not os.path.isfile(pdf_file):
            logging.warning(f"File not found: {pdf_file}")
            continue
        
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            logging.info(f"Adding {pdf_file} with {len(pdf_reader.pages)} pages")
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
        except PyPDF2.utils.PdfReadError as e:
            logging.error(f"Error reading {pdf_file}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error with {pdf_file}: {e}")
    
    # Save the merged PDF before adding page numbers
    temp_output_pdf = 'temp_merged_notes.pdf'
    try:
        with open(temp_output_pdf, 'wb') as out_file:
            pdf_writer.write(out_file)
        logging.info(f'Merged PDF saved as {temp_output_pdf}')
    except Exception as e:
        logging.error(f"Error saving merged PDF: {e}")
        return
    
    # Add page numbers to the merged PDF
    add_page_numbers(temp_output_pdf, output_pdf, start_number=1, skip_first_pages=3)
    
    # Optionally, remove the temporary file
    if os.path.isfile(temp_output_pdf):
        os.remove(temp_output_pdf)

def main():
    # Specify paths for the PDFs in the required order
    pdf_files = [
        'cover.pdf',
        # Adding day 1 to day 15 PDFs
        *[f'AI Day {str(day).zfill(2)} Notes.pdf' for day in range(1, 16)],
        'match case statement.pdf', # Added after day 5
        'os module.pdf',
        'collection module.pdf',
        '100 python exam questions.pdf',
        '85 exam problems.pdf',
        'end.pdf'
    ]
    
    # Output file name
    output_pdf = 'merged_notes.pdf'
    
    # Check if all files exist
    missing_files = [file for file in pdf_files if not os.path.isfile(file)]
    if missing_files:
        logging.error(f"Missing files: {', '.join(missing_files)}")
        return
    
    # Merge the PDFs
    merge_pdfs(output_pdf, pdf_files)

if __name__ == "__main__":
    main()
