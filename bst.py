class BSTNode:
    """
    Node for Binary Search Tree
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree implementation
    """

    def __init__(self):
        self.root = None

    # =====================================================
    # INSERT
    # =====================================================

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):

        if node is None:
            return BSTNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)

        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    # =====================================================
    # SEARCH
    # =====================================================

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):

        if node is None:
            return False

        if node.key == key:
            return True

        if key < node.key:
            return self._search(node.left, key)

        return self._search(node.right, key)

    # =====================================================
    # INORDER TRAVERSAL
    # =====================================================

    def inorder(self):

        result = []

        self._inorder(self.root, result)

        return result

    def _inorder(self, node, result):

        if node is not None:

            self._inorder(node.left, result)

            result.append(node.key)

            self._inorder(node.right, result)

    # =====================================================
    # SIZE
    # =====================================================

    def size(self):
        return len(self.inorder())


# =====================================================
# HELPER FUNCTION
# =====================================================

def build_bst_from_terms(terms):
    """
    Build BST from a list of terms.

    Parameters
    ----------
    terms : list

    Returns
    -------
    BinarySearchTree
    """

    bst = BinarySearchTree()

    for term in terms:
        bst.insert(term)

    return bst


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    terms = [
        "machine",
        "learning",
        "python",
        "azure",
        "analytics",
        "streamlit"
    ]

    bst = build_bst_from_terms(terms)

    print("Sorted Terms:")
    print(bst.inorder())

    print("\nSearch machine:")
    print(bst.search("machine"))

    print("\nSearch tensorflow:")
    print(bst.search("tensorflow"))

    print("\nTree Size:")
    print(bst.size())