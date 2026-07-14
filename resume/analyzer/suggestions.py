import re

def find_missing_skills(detected_skills, target_skills):

    missing = []
    for skill in target_skills:
        if skill not in detected_skills:
            missing.append(skill)

    return missing

def experience_suggestion(text):

    match = re.search(r"(\d+)\s+years?", text.lower())

    if not match:
        return "Add your work experience if you have any."
    years = int(match.group(1))

    if years < 2:
        return "Add more project experience to strengthen your resume."

    return None

def keyword_suggestions(missing_skills):

    suggestions = []
    for skill in missing_skills:
        suggestions.append(
            f"Consider adding '{skill}' to your resume if you have worked with it."
        )

    return suggestions

def generate_suggestions(
    detected_skills,
    target_skills,
    resume_text,
):

    suggestions = []

    missing = find_missing_skills(
        detected_skills,
        target_skills,
    )

    keyword_feedback = keyword_suggestions(missing)

    suggestions.extend(keyword_feedback)

    experience_feedback = experience_suggestion(
        resume_text
    )

    if experience_feedback:
        suggestions.append(experience_feedback)

    return suggestions