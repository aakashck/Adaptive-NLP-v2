import re

WORD_TOKEN_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?|[0-9]+|[^\sA-Za-z0-9]+")

SIMPLE_DICT = {
    "advancement": "progress",
    "technologies": "technology",
    "impacted": "affected",
    "sectors": "areas",
    "including": "such as",
    "significant": "important",
    "various": "different",
    "artificial": "man-made",
    "intelligence": "smart",
    "rapid": "fast",
    "technologies": "technology",
    "complexity": "difficulty",
    "analyzes": "checks",
    "analysis": "review",
    "simplification": "simplifying",
    "processing": "working",
    "real-time": "instant",
    "environment": "setting"
}

PUNCTUATION = {'.', ',', '!', '?', ':', ';', '"', "'", '(', ')', '[', ']', '{', '}', '—', '–'}

def simplify_word(word):
    word_lower = word.lower()
    if word_lower in SIMPLE_DICT:
        return SIMPLE_DICT[word_lower]
    return word


def simplify_text(text):
    tokens = WORD_TOKEN_PATTERN.findall(text)
    simplified_tokens = []
    for token in tokens:
        if token in PUNCTUATION:
            if simplified_tokens:
                simplified_tokens[-1] += token
            else:
                simplified_tokens.append(token)
        else:
            simplified_tokens.append(simplify_word(token))
    return " ".join(simplified_tokens)
