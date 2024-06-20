import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    # Open the provided PDF file
    document = fitz.open(pdf_path)

    # Initialize an empty string to store the extracted text
    text = ""

    # Iterate through each page of the PDF
    for page_num in range(len(document)):
        page = document.load_page(page_num)

        # Extract text from the page and append to the result string
        text += page.get_text()

    # Close the PDF document
    document.close()

    return text


# Example usage:
pdf_path = "/path/to/your/pdf/document.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)
