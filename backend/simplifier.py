import re
from nltk.corpus import wordnet

WORD_TOKEN_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?|[0-9]+|[^\sA-Za-z0-9]+")

SIMPLE_DICT = {
    "advancement": "progress",
    "technologies": "tech",
    "impacted": "affected",
    "sectors": "areas",
    "including": "such as",
    "significant": "important",
    "various": "different",
    "artificial": "man-made",
    "intelligence": "smarts",
    "rapid": "fast"
}

def simplify_word(word):
    word_lower = word.lower()
    if word_lower in SIMPLE_DICT:
        return SIMPLE_DICT[word_lower]
    synsets = wordnet.synsets(word)
    if synsets:
        lemmas = synsets[0].lemmas()
        if lemmas:
            simple = lemmas[0].name().replace("_", " ")
            if len(simple) < len(word) and simple != word:
                return simple
    return word

def simplify_text(text):
    tokens = WORD_TOKEN_PATTERN.findall(text)
    simplified_tokens = [simplify_word(token) for token in tokens]
    return " ".join(simplified_tokens)
