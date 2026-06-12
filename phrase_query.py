from collections import defaultdict
import pandas as pd


# =====================================================
# BIWORD INDEX
# =====================================================

def build_biword_index(documents):
    """
    Build biword index.

    Example:
    machine learning is fun

    Creates:
    machine learning
    learning is
    is fun
    """

    biword_index = defaultdict(set)

    for doc_id, tokens in documents.items():

        for i in range(len(tokens) - 1):

            biword = f"{tokens[i]} {tokens[i+1]}"

            biword_index[biword].add(doc_id)

    return {
        biword: sorted(list(doc_ids))
        for biword, doc_ids in biword_index.items()
    }


# =====================================================
# BIWORD SEARCH
# =====================================================

def search_biword(query, biword_index):
    """
    Supports:
    machine learning
    machine learning algorithms
    """

    query_terms = query.lower().split()

    # Single word query
    if len(query_terms) < 2:
        return []

    # Build query biwords
    query_biwords = []

    for i in range(len(query_terms) - 1):

        query_biwords.append(
            f"{query_terms[i]} {query_terms[i+1]}"
        )

    result_docs = None

    for biword in query_biwords:

        docs = set(
            biword_index.get(biword, [])
        )

        if result_docs is None:

            result_docs = docs

        else:

            result_docs &= docs

    return sorted(list(result_docs)) \
        if result_docs else []


# =====================================================
# POSITIONAL INDEX
# =====================================================

def build_positional_index(documents):

    positional_index = defaultdict(
        lambda: defaultdict(list)
    )

    for doc_id, tokens in documents.items():

        for position, token in enumerate(tokens):

            positional_index[token][doc_id].append(
                position
            )

    return positional_index


# =====================================================
# POSITIONAL SEARCH
# =====================================================

def search_positional_phrase(
    query,
    positional_index
):

    query_terms = query.lower().split()

    if len(query_terms) == 0:
        return []

    # Single word query
    if len(query_terms) == 1:

        term = query_terms[0]

        if term in positional_index:

            return sorted(
                positional_index[term].keys()
            )

        return []

    # Candidate docs

    if query_terms[0] not in positional_index:
        return []

    candidate_docs = set(
        positional_index[
            query_terms[0]
        ].keys()
    )

    for term in query_terms[1:]:

        if term not in positional_index:
            return []

        candidate_docs &= set(
            positional_index[
                term
            ].keys()
        )

    matching_docs = []

    for doc_id in candidate_docs:

        first_positions = positional_index[
            query_terms[0]
        ][doc_id]

        for start_pos in first_positions:

            phrase_found = True

            for offset in range(
                1,
                len(query_terms)
            ):

                term = query_terms[offset]

                if (
                    start_pos + offset
                    not in positional_index[
                        term
                    ][doc_id]
                ):
                    phrase_found = False
                    break

            if phrase_found:

                matching_docs.append(
                    doc_id
                )

                break

    return sorted(matching_docs)


# =====================================================
# BIWORD DATAFRAME
# =====================================================

def biword_index_dataframe(
    biword_index
):

    rows = []

    for biword, docs in biword_index.items():

        rows.append({
            "Biword": biword,
            "Documents": ", ".join(docs)
        })

    return pd.DataFrame(rows)


# =====================================================
# POSITIONAL DATAFRAME
# =====================================================

def positional_index_to_dataframe(
    positional_index
):

    rows = []

    for term, doc_info in positional_index.items():

        for doc_id, positions in doc_info.items():

            rows.append({
                "Term": term,
                "Document": doc_id,
                "Positions": positions
            })

    return pd.DataFrame(rows)