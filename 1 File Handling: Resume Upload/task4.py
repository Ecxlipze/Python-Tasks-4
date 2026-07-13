import os

ALLOWED_EXTENSIONS = [".pdf", ".docx"]

def validate_file(file_path):
    if not os.path.exists(file_path):
        return False, "File does not exist."

    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension not in ALLOWED_EXTENSIONS:
        return False, "Unsupported file type."
    return True, "File is valid."