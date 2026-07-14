import re

SKILLS_WEIGHT = 40
EXPERIENCE_WEIGHT = 30
KEYWORDS_WEIGHT = 30

def score_skills(detected_skills, total_required_skills):

    if total_required_skills == 0:
        return 0
    score = (len(detected_skills) / total_required_skills) * SKILLS_WEIGHT

    return round(score, 2)

def score_experience(text):

    match = re.search(r"(\d+)\s+years?", text.lower())
    if not match:
        return 0
    years = int(match.group(1))

    if years >= 5:
        return EXPERIENCE_WEIGHT

    return round((years / 5) * EXPERIENCE_WEIGHT, 2)

def normalize_score(score):

    if score < 0:
        return 0
    if score > 100:
        return 100

    return round(score, 2)

def calculate_resume_score(skill_score, experience_score, keyword_score):

    total = skill_score + experience_score + keyword_score
    return normalize_score(total)