# job_parser.py
def parse_job(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error parsing job file: {e}")
        return ""
