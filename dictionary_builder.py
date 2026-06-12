def extract_unique_terms(documents):
    """
    Extract all unique terms from the document collection.

    Parameters
    ----------
    documents : dict

    Example:
    {
        "doc1": ["machine", "learning"],
        "doc2": ["machine", "vision"]
    }

    Returns
    -------
    list

    Example:
    [
        "learning",
        "machine",
        "vision"
    ]
    """

    unique_terms = set()

    for tokens in documents.values():
        unique_terms.update(tokens)

    return sorted(unique_terms)