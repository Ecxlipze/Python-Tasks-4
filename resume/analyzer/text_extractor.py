import os
from PyPDF2 import PdfReader
from docx import Document

def extract_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    if not text.strip():
        return None

    return text

def extract_docx_text(file_path):

    document = Document(file_path)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def text_statistics(text):
    
    characters = len(text)
    words = len(text.split())

    return {
        "characters": characters,
        "words": words,
    }


def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()
    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    return None