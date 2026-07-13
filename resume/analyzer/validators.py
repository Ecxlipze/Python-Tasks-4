import os

ALLOWED_EXTENSIONS = [".pdf", ".docx"]

def validate_resume(uploaded_file):

    if uploaded_file is None:
        return False, "No file uploaded."

    extension = os.path.splitext(uploaded_file.name)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        return False, "Only PDF and DOCX files are allowed."

    return True, "File is valid."