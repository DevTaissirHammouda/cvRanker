import pdfplumber

def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text() + "\n"
    return extracted_text.strip()

# Example Usage
pdf_file = "taissirCV.pdf"
text = extract_text_from_pdf(pdf_file)
print(text)
