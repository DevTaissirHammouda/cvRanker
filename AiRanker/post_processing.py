def filter_entities(entities):
    filtered_entities = []
    for entity in entities:
        # Remove subword tokens or broken entities
        if "##" not in entity["word"]:
            filtered_entities.append(entity)
    return filtered_entities
