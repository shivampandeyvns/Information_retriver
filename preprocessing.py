import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download required resources (runs only first time)
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Initialize objects
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def handle_hyphens(text):
    """
    Convert hyphenated words into space-separated words.
    Example:
    state-of-the-art -> state of the art
    """
    return re.sub(r"-", " ", text)


def tokenize_text(text):
    """
    Tokenize text into words.
    """
    return word_tokenize(text)


def lowercase_tokens(tokens):
    """
    Convert all tokens to lowercase.
    """
    return [token.lower() for token in tokens]


def remove_stopwords(tokens):
    """
    Remove English stopwords.
    """
    return [token for token in tokens if token not in stop_words]


def remove_punctuation(tokens):
    """
    Keep only alphanumeric words.
    """
    return [token for token in tokens if token.isalnum()]


def stem_tokens(tokens):
    """
    Apply Porter Stemmer.
    """
    return [stemmer.stem(token) for token in tokens]


def lemmatize_tokens(tokens):
    """
    Apply WordNet Lemmatizer.
    """
    return [lemmatizer.lemmatize(token) for token in tokens]


def preprocess_document(text, method="lemmatization"):
    """
    Complete preprocessing pipeline.

    Parameters
    ----------
    text : str
    method : str
        'stemming' or 'lemmatization'

    Returns
    -------
    dict
        Contains outputs of each preprocessing stage.
    """

    hyphen_processed = handle_hyphens(text)

    tokens = tokenize_text(hyphen_processed)

    lower_tokens = lowercase_tokens(tokens)

    clean_tokens = remove_punctuation(lower_tokens)

    stopword_removed = remove_stopwords(clean_tokens)

    if method == "stemming":
        final_tokens = stem_tokens(stopword_removed)

    elif method == "lemmatization":
        final_tokens = lemmatize_tokens(stopword_removed)

    else:
        raise ValueError(
            "method must be 'stemming' or 'lemmatization'"
        )

    return {
        "original_text": text,
        "tokens": tokens,
        "lowercase_tokens": lower_tokens,
        "stopword_removed": stopword_removed,
        "final_tokens": final_tokens
    }