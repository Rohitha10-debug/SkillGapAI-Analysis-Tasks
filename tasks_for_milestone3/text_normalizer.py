def normalize_skills(skills):
    mapping = {
        "ml": "machine learning",
        "dl": "deep learning",
        "ai": "artificial intelligence"
    }

    normalized = set()
    for skill in skills:
        s = skill.lower().strip()
        s = mapping.get(s, s)
        normalized.add(s)

    return list(normalized)
