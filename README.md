# PDF Merge and Page Numbering Script

This Python script allows you to merge multiple PDF files into a single document and add page numbers, with custom options for starting the page numbering and skipping initial pages. The script uses the `pikepdf` library for PDF manipulation and `reportlab` for adding page numbers.

## Overview

The script performs the following tasks:
1. Merges multiple PDF files in a specified order.
2. Adds page numbers to the merged PDF, starting from a specified number and skipping a certain number of initial pages.

## Features

- **Custom Order**: Merge PDFs in the order specified by the user.
- **Page Numbering**: Add page numbers starting from a specific number, with options to skip initial pages.

## Requirements

- Python 3.x
- `pikepdf`
- `reportlab`

To install the required libraries, use the following command:

```bash
pip install pikepdf reportlab
```

## Usage

### 1. Script Description

The script includes the following main functions:

- `merge_pdfs(output_pdf, pdf_files)`: Merges the specified PDF files in the given order.
- `add_page_numbers(input_pdf, output_pdf, start_number=1, skip_first_pages=3)`: Adds page numbers to the merged PDF, skipping a specified number of initial pages and starting numbering from a given number.

### 2. Running the Script

To run the script, use the command line to specify the output PDF file and a list of PDF files to merge:

```bash
python main2.py <output_pdf> <pdf_file1> <pdf_file2> ...
```

**Example**:

```bash
python main2.py merged_notes_with_custom_page_numbers.pdf cover.pdf "AI Day 01 Notes.pdf" "AI Day 02 Notes.pdf" "match case statement.pdf" "os module.pdf" "collection module.pdf" "100 python exam questions.pdf" "85 exam problems.pdf" end.pdf
```

### 3. Parameters

- `output_pdf`: The name of the final merged PDF file.
- `pdf_files`: A list of PDF files to merge in the specified order.

### 4. Customizing Page Numbering

The `add_page_numbers` function parameters:
- `input_pdf`: Path to the temporary merged PDF file.
- `output_pdf`: Path where the final PDF with page numbers will be saved.
- `start_number`: The starting number for page numbering (default is 1).
- `skip_first_pages`: Number of initial pages to skip for numbering (default is 3).

Adjust these parameters in the `main()` function if needed.

## Example

To merge the following files:

- `cover.pdf`
- `AI Day 01 Notes.pdf`
- `AI Day 02 Notes.pdf`
- ...
- `AI Day 15 Notes.pdf`
- `match case statement.pdf`
- `os module.pdf`
- `collection module.pdf`
- `100 python exam questions.pdf`
- `85 exam problems.pdf`
- `end.pdf`

Run the script as shown in the "Running the Script" section. The script will create a merged PDF and add page numbers, skipping the first 3 pages and starting numbering from 1.

## Troubleshooting

- Ensure all specified PDF files exist in the same directory as the script.
- Verify that the required libraries are correctly installed and up to date.
- Ensure the script has appropriate permissions to read and write files in the directory.

## License

This script is provided as-is. You are free to modify and use it according to your needs.

## Repository

You can find the repository for this script at [GitHub - cyberfantics/merge-pdf-files](https://github.com/cyberfantics/merge-pdf-files/).

## Developer
Syed Mansoor ul Hassan Bukhari
