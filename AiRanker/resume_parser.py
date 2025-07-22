# resume_parser.py
from pdfminer.high_level import extract_text

def parse_resume(path):
    try:
        text = extract_text(path)
        return text
    except Exception as e:
        print(f"Error parsing {path}: {e}")
        return ""
