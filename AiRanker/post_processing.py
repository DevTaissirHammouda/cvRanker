def filter_entities(entities):
    """Filter out broken or irrelevant entities."""
    filtered_entities = []
    for entity in entities:
        # Remove subword tokens or broken entities
        if "##" not in entity["word"]:
            filtered_entities.append(entity)
    return filtered_entities
