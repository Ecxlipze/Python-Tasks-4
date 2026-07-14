import os

from analyzer.text_extractor import (
    extract_pdf_text,
    extract_docx_text,
)
from analyzer.preprocessing import preprocess_text
from analyzer.skill_detector import detect_skills, SKILLS
from analyzer.scorer import (
    score_skills,
    score_experience,
    calculate_resume_score,
)
from analyzer.suggestions import generate_suggestions


def analyze_resume(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        text = extract_pdf_text(file_path)

    elif extension == ".docx":
        text = extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported file format.")

    tokens = preprocess_text(text)

    detected_skills = detect_skills(tokens)

    skill_score = score_skills(
        detected_skills,
        len(SKILLS),
    )

    experience_score = score_experience(text)

    keyword_score = 0

    total_score = calculate_resume_score(
        skill_score,
        experience_score,
        keyword_score,
    )

    suggestions = generate_suggestions(
        detected_skills,
        SKILLS,
        text,
    )

    return {
        "score": total_score,
        "skills": detected_skills,
        "suggestions": suggestions,
    }