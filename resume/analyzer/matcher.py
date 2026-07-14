from analyzer.preprocessing import preprocess_text
from analyzer.skill_detector import detect_skills
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from analyzer.suggestions import find_missing_skills

def process_job_description(job_description):

    return preprocess_text(job_description)

def extract_job_keywords(job_description):

    tokens = preprocess_text(job_description)
    keywords = detect_skills(tokens)
    return keywords

def calculate_match_percentage(
    resume_skills,
    job_keywords,
):

    if len(job_keywords) == 0:
        return 0
    matched = 0

    for skill in job_keywords:
        if skill in resume_skills:
            matched += 1

    percentage = (
        matched / len(job_keywords)
    ) * 100

    return round(percentage, 2)

def calculate_similarity(resume_text, job_description):

    documents = [
        resume_text,
        job_description,
    ]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents).toarray() # type: ignore

    similarity = cosine_similarity(
        [tfidf_matrix[0]], # pyright: ignore[reportArgumentType]
        [tfidf_matrix[1]], # pyright: ignore[reportArgumentType]
    )

    return round(float(similarity[0][0]) * 100, 2)

def analyze_job_match(
    resume_skills,
    job_keywords,
):

    match_percentage = calculate_match_percentage(
        resume_skills,
        job_keywords,
    )
    missing_keywords = find_missing_skills(
        resume_skills,
        job_keywords,
    )
    return {
        "match_percentage": match_percentage,
        "missing_keywords": missing_keywords,
    }