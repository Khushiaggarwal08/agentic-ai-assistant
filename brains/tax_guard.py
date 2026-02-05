FORBIDDEN_PHRASES = [
    "male",
    "female",
    "marriage",
    "inheritance",
    "succession",
    "inter-generational",
    "without clubbing",
    "avoids clubbing",
    "automatic tax saving",
    "capital gains exemption",
    "family traditions",
    "karta led",
    "joint owners"
]

def is_tax_answer_safe(answer: str) -> bool:
    text = answer.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in text:
            return False
    return True
