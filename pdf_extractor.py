import pdfplumber
import re
import base64
import io

def pdf_to_base64(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode("utf-8")

def smart_paragraph_split(text):
    """Splits paragraphs using sentence-ending punctuation and line breaks."""
    return re.split(r'(?<=\.)\s*\n', text)  # Split at periods followed by newlines

# def extract_paragraphs_from_pdf(pdf_path):
def extract_paragraphs_from_base64(pdf_base64):
# def extract_paragraphs_from_base64(pdf_bytes):    
    text = ""
    pdf_bytes = base64.b64decode(pdf_base64)
    # with pdfplumber.open(pdf_path) as pdf:
    bytes = io.BytesIO()
    bytes.write(pdf_bytes)
    with pdfplumber.open(bytes) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"  # Extract text from each page

    # Split text into paragraphs (by double newlines or empty lines)
    paragraphs = [para.strip() for para in smart_paragraph_split(text=text) if para.strip()]
    return paragraphs

# Example Usage
# pdf_file = "171120231905-CorrigendumFormats.pdf"  # Replace with your PDF file path
# paragraphs = extract_paragraphs_from_pdf(pdf_file)
# sample_base64_pdf = pdf_to_base64(pdf_file)
# paragraphs = extract_paragraphs_from_base64(sample_base64_pdf)

# for i, para in enumerate(paragraphs):  # Print first 5 paragraphs
#     print(f"Paragraph {i}: {para}\n")
