from bisect import bisect_left


class BTreeDictionary:
    """
    Simplified B-Tree style dictionary using
    sorted terms and binary search.
    """

    def __init__(self):
        self.terms = []

    # ==========================================
    # INSERT
    # ==========================================

    def insert(self, term):
        self.terms.append(term)

    # ==========================================
    # FINALIZE
    # ==========================================

    def finalize(self):
        self.terms = sorted(set(self.terms))

    # ==========================================
    # SEARCH
    # ==========================================

    def search(self, term):

        index = bisect_left(self.terms, term)

        return (
            index < len(self.terms)
            and self.terms[index] == term
        )

    # ==========================================
    # GET TERMS
    # ==========================================

    def get_terms(self):
        return self.terms

    # ==========================================
    # SIZE
    # ==========================================

    def size(self):
        return len(self.terms)


# ==========================================
# HELPER FUNCTION
# ==========================================

def build_btree_from_terms(terms):
    """
    Build B-Tree dictionary from list of terms.
    """

    btree = BTreeDictionary()

    for term in terms:
        btree.insert(term)

    btree.finalize()

    return btree


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    terms = [
        "machine",
        "learning",
        "python",
        "azure",
        "analytics",
        "streamlit"
    ]

    btree = build_btree_from_terms(terms)

    print("Terms:")
    print(btree.get_terms())

    print("\nSearch machine:")
    print(btree.search("machine"))

    print("\nSearch tensorflow:")
    print(btree.search("tensorflow"))

    print("\nSize:")
    print(btree.size())