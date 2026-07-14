import os

SUPPORTED_EXTENSIONS = (".pdf", ".docx")

def get_resume_files(folder_path):
    resumes = []
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(SUPPORTED_EXTENSIONS):
            resumes.append(file_name)

    return resumes

def sort_resumes(results):

    return sorted(
        results,
        key=lambda resume: resume["score"],
        reverse=True,
    )
    
def rank_against_job(results):

    return sorted(
        results,
        key=lambda resume: resume["match_percentage"],
        reverse=True,
    )
    
def safe_process_resume(file_name, process_function):

    try:
        return process_function(file_name)

    except Exception as error:
        print(f"Could not process {file_name}: {error}")

        return None
    
def display_ranking(results):

    print("-" * 70)
    print(f"{'Rank':<6}{'Resume':<35}{'Score':<10}{'Match %'}")
    print("-" * 70)

    for index, resume in enumerate(results, start=1):
        print(
            f"{index:<6}"
            f"{resume['name']:<35}"
            f"{resume['score']:<10}"
            f"{resume['match_percentage']}%"
        )

    print("-" * 70)