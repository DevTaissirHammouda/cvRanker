# resume_parser.py
from pdfminer.high_level import extract_text

# print("resume_parser module loaded ✅")  # Debug line

def parse_resume(path):
    try:
        text = extract_text(path)
        return text
    except Exception as e:
        print(f"Error parsing {path}: {e}")
        return ""

# Temporary test
# if __name__ == "__main__":
#     print(parse_resume("data/resumes/taissirCv.pdf"))
