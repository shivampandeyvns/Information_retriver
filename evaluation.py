import time
import pandas as pd

from bst import build_bst_from_terms
from btree_index import build_btree_from_terms


def compare_bst_btree(unique_terms, queries):
    """
    Compare search performance of BST and B-Tree.

    Parameters
    ----------
    unique_terms : list
        List of unique terms from the document collection

    queries : list
        Search queries to test

    Returns
    -------
    pandas.DataFrame
    """

    bst = build_bst_from_terms(unique_terms)
    btree = build_btree_from_terms(unique_terms)

    results = []

    for query in queries:

        # BST Timing
        start = time.perf_counter()
        bst_result = bst.search(query)
        bst_time = (time.perf_counter() - start) * 1000

        # B-Tree Timing
        start = time.perf_counter()
        btree_result = btree.search(query)
        btree_time = (time.perf_counter() - start) * 1000

        results.append({
            "Query": query,
            "Found in BST": bst_result,
            "Found in B-Tree": btree_result,
            "BST Time (ms)": round(bst_time, 6),
            "B-Tree Time (ms)": round(btree_time, 6)
        })

    return pd.DataFrame(results)


def summarize_bst_btree(results_df):
    """
    Generate summary statistics.
    """

    return pd.DataFrame([{
        "Average BST Time (ms)":
            round(results_df["BST Time (ms)"].mean(), 6),

        "Average B-Tree Time (ms)":
            round(results_df["B-Tree Time (ms)"].mean(), 6)
    }])


# Example usage
if __name__ == "__main__":

    unique_terms = [
        "machine",
        "learning",
        "python",
        "streamlit",
        "azure",
        "analytics",
        "data",
        "science",
        "retrieval",
        "indexing"
    ]

    queries = [
        "machine",
        "python",
        "azure",
        "tensorflow",
        "analytics"
    ]

    results = compare_bst_btree(
        unique_terms,
        queries
    )

    print("\nDetailed Results")
    print(results)

    print("\nSummary")
    print(summarize_bst_btree(results))