from collections import defaultdict
from nltk.metrics.distance import edit_distance
import pandas as pd


# =====================================================
# SPELL CORRECTION USING EDIT DISTANCE
# =====================================================

def spell_correction(word, vocabulary):
    """
    Find the closest matching word using edit distance.
    """

    word = word.lower()

    best_match = None
    min_distance = float("inf")

    for vocab_word in vocabulary:

        distance = edit_distance(word, vocab_word)

        if distance < min_distance:
            min_distance = distance
            best_match = vocab_word

    return best_match, min_distance


# =====================================================
# WILDCARD SEARCH
# =====================================================

def wildcard_search(pattern, vocabulary):
    """
    Supports:
    mach*
    *ing
    *learn*
    """

    pattern = pattern.lower()

    results = []

    # Contains
    if pattern.startswith("*") and pattern.endswith("*"):

        substring = pattern.strip("*")

        for word in vocabulary:
            if substring in word:
                results.append(word)

    # Ends with
    elif pattern.startswith("*"):

        suffix = pattern[1:]

        for word in vocabulary:
            if word.endswith(suffix):
                results.append(word)

    # Starts with
    elif pattern.endswith("*"):

        prefix = pattern[:-1]

        for word in vocabulary:
            if word.startswith(prefix):
                results.append(word)

    else:

        if pattern in vocabulary:
            results.append(pattern)

    return sorted(results)


# =====================================================
# K-GRAM GENERATION
# =====================================================

def generate_kgrams(word, k=3):
    """
    Generate k-grams from a word.

    Example:
    machine -> ['$ma', 'mac', 'ach', ...]
    """

    word = f"${word}$"

    grams = []

    for i in range(len(word) - k + 1):
        grams.append(word[i:i+k])

    return grams


# =====================================================
# BUILD K-GRAM INDEX
# =====================================================

def build_kgram_index(vocabulary, k=3):
    """
    Build K-Gram Index.
    """

    kgram_index = defaultdict(set)

    for word in vocabulary:

        grams = generate_kgrams(word, k)

        for gram in grams:
            kgram_index[gram].add(word)

    return {
        gram: sorted(list(words))
        for gram, words in kgram_index.items()
    }


# =====================================================
# K-GRAM SEARCH
# =====================================================

def kgram_search(word, kgram_index, k=3):
    """
    Find candidate words using K-Grams.
    """

    grams = generate_kgrams(word, k)

    candidates = set()

    for gram in grams:

        if gram in kgram_index:
            candidates.update(kgram_index[gram])

    return sorted(candidates)


# =====================================================
# DATAFRAME FOR STREAMLIT DISPLAY
# =====================================================

def kgram_dataframe(kgram_index):
    """
    Convert K-Gram Index into DataFrame.
    """

    rows = []

    for gram, words in kgram_index.items():

        rows.append({
            "K-Gram": gram,
            "Terms": ", ".join(words)
        })

    return pd.DataFrame(rows)


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    vocabulary = [
        "machine",
        "machinery",
        "learning",
        "retrieval",
        "python",
        "analytics",
        "streamlit"
    ]

    print("SPELL CORRECTION")
    print(
        spell_correction(
            "machien",
            vocabulary
        )
    )

    print("\nWILDCARD SEARCH")
    print(
        wildcard_search(
            "mach*",
            vocabulary
        )
    )

    print("\nK-GRAM INDEX")

    kgram_index = build_kgram_index(
        vocabulary
    )

    print(
        kgram_search(
            "machien",
            kgram_index
        )
    )

    print("\nK-GRAM DATAFRAME")

    print(
        kgram_dataframe(
            kgram_index
        ).head()
    )