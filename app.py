
import streamlit as st
import pandas as pd

from preprocessing import preprocess_document
from indexing import (
    build_inverted_index,
    get_index_dataframe,
    search_and_query
)

from phrase_query import (
    build_biword_index,
    build_positional_index,
    search_biword,
    search_positional_phrase
)

from dictionary_builder import extract_unique_terms

from evaluation import (
    compare_bst_btree,
    summarize_bst_btree
)

from tolerant_retrieval import (
    spell_correction,
    wildcard_search,
    build_kgram_index,
    kgram_dataframe
)

from file_loader import load_uploaded_files

st.set_page_config(
    page_title="Information Retrieval System",
    layout="wide"
)

st.title("Information Retrieval System")

uploaded_files = st.sidebar.file_uploader(
    "Upload Text Documents",
    type=["txt"],
    accept_multiple_files=True
)

if not uploaded_files:
    st.info("Upload documents to begin")
    st.stop()

raw_documents = load_uploaded_files(uploaded_files)

# Stem docs
stem_docs = {}
for doc_name, text in raw_documents.items():
    result = preprocess_document(text, method="stemming")
    stem_docs[doc_name] = result["final_tokens"]

# Lemma docs
lemma_docs = {}
for doc_name, text in raw_documents.items():
    result = preprocess_document(text, method="lemmatization")
    lemma_docs[doc_name] = result["final_tokens"]

stem_terms = extract_unique_terms(stem_docs)
lemma_terms = extract_unique_terms(lemma_docs)

preprocessed_docs = lemma_docs

inverted_index = build_inverted_index(preprocessed_docs)
biword_index = build_biword_index(preprocessed_docs)
positional_index = build_positional_index(preprocessed_docs)
unique_terms = extract_unique_terms(preprocessed_docs)

tabs = st.tabs([
    "Documents",
    "Preprocessing",
    "Stem vs Lemma",
    "Inverted Index",
    "Phrase Query",
    "BST vs BTree",
    "Tolerant Retrieval",
    "Inference"
])

with tabs[0]:
    st.header("Uploaded Documents")
    for doc_name, text in raw_documents.items():
        with st.expander(doc_name):
            st.write(text)

with tabs[1]:
    st.header("Preprocessing")
    selected_doc = st.selectbox(
        "Select Document",
        list(raw_documents.keys())
    )

    result = preprocess_document(
        raw_documents[selected_doc],
        method="lemmatization"
    )

    st.subheader("Tokens")
    st.write(result["tokens"])

    st.subheader("Lowercase")
    st.write(result["lowercase_tokens"])

    st.subheader("Stopword Removed")
    st.write(result["stopword_removed"])

    st.subheader("Final Tokens")
    st.write(result["final_tokens"])

with tabs[2]:
    st.header("Stemming vs Lemmatization")

    selected_doc = st.selectbox(
        "Select Document",
        list(raw_documents.keys()),
        key="stem_lemma_doc"
    )

    stem_result = preprocess_document(
        raw_documents[selected_doc],
        method="stemming"
    )

    lemma_result = preprocess_document(
        raw_documents[selected_doc],
        method="lemmatization"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Stemming")
        st.write(stem_result["final_tokens"])
        st.metric(
            "Unique Terms",
            len(set(stem_result["final_tokens"]))
        )

    with col2:
        st.subheader("Lemmatization")
        st.write(lemma_result["final_tokens"])
        st.metric(
            "Unique Terms",
            len(set(lemma_result["final_tokens"]))
        )

    comparison_df = pd.DataFrame({
        "Metric": ["Unique Terms"],
        "Stemming": [len(stem_terms)],
        "Lemmatization": [len(lemma_terms)]
    })

    st.subheader("Corpus Statistics")
    st.dataframe(comparison_df)

    query = st.text_input(
        "Enter Query",
        key="stem_lemma_query"
    )

    if query:
        stem_index = build_inverted_index(stem_docs)
        lemma_index = build_inverted_index(lemma_docs)

        stem_results = search_and_query(query, stem_index)
        lemma_results = search_and_query(query, lemma_index)

        st.dataframe(pd.DataFrame({
            "Method": ["Stemming", "Lemmatization"],
            "Retrieved Documents": [
                str(stem_results),
                str(lemma_results)
            ],
            "Document Count": [
                len(stem_results),
                len(lemma_results)
            ]
        }))

with tabs[3]:
    st.header("Inverted Index")

    st.dataframe(
        get_index_dataframe(inverted_index)
    )

    query = st.text_input(
        "Search Term",
        key="index_query"
    )

    if query:
        results = search_and_query(
            query,
            inverted_index
        )
        st.write(results)

with tabs[4]:
    st.header("Phrase Query Search")

    phrase = st.text_input(
        "Enter Phrase Query"
    )

    if phrase:

        if len(phrase.split()) < 2:
            st.warning(
                "Biword Index works on phrases containing at least two words."
            )

        biword_results = search_biword(
            phrase,
            biword_index
        )

        positional_results = search_positional_phrase(
            phrase,
            positional_index
        )

        st.dataframe(pd.DataFrame({
            "Method": ["Biword", "Positional"],
            "Results": [
                str(biword_results),
                str(positional_results)
            ]
        }))

with tabs[5]:
    st.header("BST vs BTree Comparison")

    st.metric(
        "Dictionary Size",
        len(unique_terms)
    )

    st.subheader("Sample Dictionary Terms")
    st.write(unique_terms[:50])

    sample_queries = unique_terms[:10]

    results_df = compare_bst_btree(
        unique_terms,
        sample_queries
    )

    st.dataframe(results_df)

    st.subheader("Summary")
    st.dataframe(
        summarize_bst_btree(results_df)
    )

with tabs[6]:
    st.header("Tolerant Retrieval")

    user_word = st.text_input(
        "Enter Word"
    )

    if user_word:
        correction, distance = spell_correction(
            user_word,
            unique_terms
        )

        st.write(f"Suggestion: {correction}")
        st.write(f"Edit Distance: {distance}")

    wildcard = st.text_input(
        "Wildcard Query"
    )

    if wildcard:
        st.write(
            wildcard_search(
                wildcard,
                unique_terms
            )
        )

    kgram_index = build_kgram_index(
        unique_terms
    )

    st.subheader("K-Gram Index")
    st.dataframe(
        kgram_dataframe(kgram_index)
    )

with tabs[7]:
    st.header("Inference")

    st.markdown("""

1. Which Preprocessing Technique Improved Retrieval Quality?

Inference

Among the preprocessing techniques applied, stop-word removal significantly improved retrieval quality by eliminating frequently occurring but semantically insignificant words such as “is”, “the”, and “of”. This reduced noise in the index and improved the relevance of retrieved documents. Lowercasing further improved consistency by ensuring that words such as “Machine” and “machine” were treated as the same term. Hyphen handling helped normalize compound expressions and improved term matching during search.

⸻

2. Was Stemming or Lemmatization Better?

Inference

Both stemming and lemmatization reduced vocabulary size and improved retrieval efficiency. However, lemmatization produced more meaningful terms because it converted words into valid dictionary forms while preserving semantic meaning. For example, words such as “running” were converted to “run” without producing artificial roots. Stemming occasionally generated non-dictionary terms such as “retriev” or “machin”, which may reduce interpretability. Based on the experimental results, lemmatization was more suitable for the selected document collection.

⸻

3. Which Phrase Query Index Was More Accurate?

Inference

The positional index provided more accurate phrase retrieval compared to the biword index. While the biword index efficiently stores adjacent word pairs and supports simple phrase queries, it may incorrectly match longer phrases because it does not explicitly verify the positions of all query terms. The positional index stores the exact location of each term within a document and validates that query terms occur in the correct sequence. Consequently, positional indexing produced more precise phrase search results.

⸻

4. Which Tree Structure Was Faster?

Inference

Experimental results indicated that the B-Tree generally achieved lower search times than the Binary Search Tree. The B-Tree maintains a balanced structure and minimizes the number of node traversals required during search operations. Although the difference was small for the current dataset due to its limited size, the performance advantage of the B-Tree is expected to increase significantly as the dictionary size grows. Therefore, B-Trees are more suitable for large-scale retrieval systems and database indexing applications.

⸻

5. How Tolerant Was the Retrieval Model?

Inference

The tolerant retrieval module successfully handled imperfect user queries through edit-distance correction, wildcard search, and K-Gram indexing. Misspelled queries such as “machien” and “retrival” were correctly mapped to “machine” and “retrieval” respectively. Wildcard queries enabled partial term matching, while the K-Gram index generated relevant candidate terms for incorrectly spelled inputs. These techniques improved the robustness of the retrieval system and enhanced the overall user search experience.

⸻

6. What Are the Limitations of the System?

Inference

The current retrieval system has several limitations. First, it relies primarily on exact term matching and does not consider semantic relationships between words. Consequently, documents containing synonyms may not be retrieved. Second, the evaluation was conducted on a relatively small document collection, which may not fully demonstrate the scalability characteristics of the indexing structures. Third, ranking mechanisms such as TF-IDF or BM25 were not implemented, meaning that documents are retrieved but not ranked by relevance.

⸻

7. How Can the System Be Improved?

Inference

Several enhancements can improve the retrieval system. TF-IDF or BM25 ranking can be incorporated to prioritize more relevant documents. Semantic retrieval techniques based on word embeddings or transformer models can improve the handling of synonyms and contextual meaning. Query expansion can further enhance recall by including related terms automatically. Finally, the system can be extended to support larger document collections, additional tolerant retrieval methods, and advanced indexing structures for improved scalability and performance.

⸻

Additional Overall Conclusion

I would add this as a final section in the report:

The project successfully implemented an end-to-end Information Retrieval system using Streamlit. The system supported document upload, preprocessing, indexing, phrase querying, dictionary search using BST and B-Tree structures, and tolerant retrieval mechanisms. Experimental analysis demonstrated the effectiveness of preprocessing techniques, the superior accuracy of positional indexing for phrase queries, the efficiency of B-Tree-based dictionary search, and the robustness provided by tolerant retrieval methods. The project provided practical insights into the design and evaluation of modern information retrieval systems while highlighting opportunities for future enhancements through ranking and semantic search techniques.
""")
