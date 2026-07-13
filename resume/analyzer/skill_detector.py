import spacy
nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python",
    "django",
    "flask",
    "fastapi",
    "java",
    "c++",
    "javascript",
    "typescript",
    "react",
    "nextjs",
    "nodejs",
    "express",
    "html",
    "css",
    "bootstrap",
    "tailwind",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "redis",
    "git",
    "github",
    "docker",
    "kubernetes",
]

def detect_skills(tokens):
    detected = []
    for token in tokens:
        if token in SKILLS and token not in detected:
            detected.append(token)
    return detected

def count_skills(skills):
    return len(skills)

def extract_entities(text):

    doc = nlp(text)
    entities = []
    for entity in doc.ents:
        entities.append(
            {
                "text": entity.text,
                "label": entity.label_,
            }
        )

    return entities