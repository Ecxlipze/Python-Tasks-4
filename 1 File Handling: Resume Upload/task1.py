import os
file_path = input("Enter file path: ")
name, extension = os.path.splitext(file_path)

extension = extension.lower()

if extension == ".pdf":
    print("PDF file detected.")
elif extension == ".docx":
    print("DOCX file detected.")
else:
    print("Unsupported file type.")