from collections import defaultdict


def build_inverted_index(documents):
    """
    Build an inverted index.

    Parameters
    ----------
    documents : dict

    Example:
    {
        "doc1": ["machine", "learning"],
        "doc2": ["learning", "python"]
    }

    Returns
    -------
    dict
    {
        "machine": ["doc1"],
        "learning": ["doc1", "doc2"],
        "python": ["doc2"]
    }
    """

    inverted_index = defaultdict(set)

    for doc_id, tokens in documents.items():

        for token in tokens:
            inverted_index[token].add(doc_id)

    return {
        term: sorted(list(doc_ids))
        for term, doc_ids in inverted_index.items()
    }


def search_inverted_index(query, inverted_index):
    """
    Search a single term.

    Example:
    query = "machine"
    """

    query = query.lower()

    return inverted_index.get(query, [])


def search_and_query(query, inverted_index):
    """
    AND search

    Example:
    machine learning

    Returns documents containing BOTH terms.
    """

    terms = query.lower().split()

    if not terms:
        return []

    result = set(inverted_index.get(terms[0], []))

    for term in terms[1:]:
        result &= set(inverted_index.get(term, []))

    return sorted(list(result))


def search_or_query(query, inverted_index):
    """
    OR search

    Example:
    machine learning

    Returns documents containing ANY term.
    """

    terms = query.lower().split()

    result = set()

    for term in terms:
        result |= set(inverted_index.get(term, []))

    return sorted(list(result))


def get_index_dataframe(inverted_index):
    """
    Convert index to dataframe for Streamlit display.
    """

    import pandas as pd

    rows = []

    for term, docs in sorted(inverted_index.items()):

        rows.append({
            "Term": term,
            "Documents": ", ".join(docs)
        })

    return pd.DataFrame(rows)