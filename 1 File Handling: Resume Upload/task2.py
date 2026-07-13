import os

file_path = input("Enter file path: ")
_, extension = os.path.splitext(file_path)
extension = extension.lower()

allowed_extensions = [".pdf", ".docx"]

if extension in allowed_extensions:
    print("File accepted.")
else:
    print("Error: Unsupported file type.")
    print("Only PDF and Docx files are allowed.")