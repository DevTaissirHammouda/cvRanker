import re


def extract_skills(text, skills_set):
    """
    Extracts skills found in the input text based on skills_set.
    Exact matching, case-insensitive.
    """
    if not text or not isinstance(text, str):
        return set()

    text_clean = text.lower()
    # Normalize text - remove punctuation except + . #
    text_clean = re.sub(r'[^a-z0-9+.# ]', ' ', text_clean)

    found_skills = set()
    # For performance, tokenize text by words + phrases could be handled by splitting on spaces
    words = set(text_clean.split())

    # Simple exact match for single-word skills
    for skill in skills_set:
        if skill in words or skill in text_clean:
            found_skills.add(skill)

    return found_skills