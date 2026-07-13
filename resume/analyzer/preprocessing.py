import string
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = text.lower()
    text = " ".join(text.split())
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    return text

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):

    filtered_tokens = []
    for token in tokens:
        if token not in STOP_WORDS:
            filtered_tokens.append(token)

    return filtered_tokens

def lemmatize(tokens):

    doc = nlp(" ".join(tokens))
    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_)

    return lemmas

def preprocess_text(text):

    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    filtered = remove_stopwords(tokens)
    lemmas = lemmatize(filtered)
    return lemmas