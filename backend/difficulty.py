import textstat

def detect_difficulty(text):
    score = textstat.flesch_reading_ease(text)

    if score > 60:
        return "Easy"
    elif score > 30:
        return "Medium"
    else:
        return "Hard"
