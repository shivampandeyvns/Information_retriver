# Information Retrieval System

## Overview

This project implements a complete Information Retrieval (IR) System using Python and Streamlit. The application demonstrates fundamental Information Retrieval concepts including text preprocessing, stemming vs lemmatization, phrase query processing, BST vs B-Tree indexing, and tolerant retrieval using K-Gram indexing.

### Features

- Text Preprocessing
- Stemming vs Lemmatization
- Inverted Index Construction
- Phrase Query Processing (Biword Index and Positional Index)
- BST vs B-Tree Performance Comparison
- Tolerant Retrieval using K-Gram Index
- Edit Distance Based Spell Correction
- Wildcard Query Processing

---

## Project Structure

```
Information_Retrieval_System/
│
├── app.py
├── preprocessing.py
├── phrase_query.py
├── tolerant_retrieval.py
├── btree_index.py
├── evaluation.py
├── requirements.txt
├── README.md
├── IR_Report.docx
│
├── documents/
    ├── doc1.txt
    ├── doc2.txt
    ├── doc3.txt
    ├── doc4.txt
    ├── doc5.txt
    ├── doc6.txt
    └── doc7.txt

```

---

## Installation

Ensure Python 3.9 or higher is installed.

Verify installation:

```
python --version
```

Install the required libraries:

```
pip install -r requirements.txt
```

### requirements.txt

```
streamlit
pandas
nltk
numpy
```

---

## Running the Application

Run the Streamlit application locally:

```
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

### Hosted Application

The application is also deployed online and can be accessed at:

https://bits-assignment-ir.streamlit.app/

---

## Using the Application

### Step 1: Upload Documents

- Upload one or more `.txt` documents.
- The uploaded documents are automatically processed and indexed.

### Step 2: Preprocessing

Navigate to the **Preprocessing** tab to view:

- Lowercasing
- Stop-word Removal
- Tokenization
- Hyphen Handling

### Step 3: Stemming vs Lemmatization

Navigate to the **Stem vs Lemma** tab.

Compare:

- Stemmed terms
- Lemmatized terms
- Vocabulary reduction

### Step 4: Phrase Query Processing

Navigate to the **Phrase Query** tab.

Example queries:

```
machine learning
artificial intelligence
```

View:

- Biword Index Representation
- Positional Index Representation
- Phrase Query Results

### Step 5: BST vs B-Tree Comparison

Navigate to the **BST vs B-Tree** tab.

Compare:

- Search Results
- Search Times
- Index Performance

Example queries:

```
access
machine
algorithm
```

### Step 6: Tolerant Retrieval

Navigate to the **Tolerant Retrieval** tab.

Example misspelled query:

```
machian
```

Example wildcard query:

```
mach*
```

View:

- Spell Correction Suggestions
- Edit Distance
- K-Gram Index Representation
- Wildcard Query Results

---

## Modules Implemented

### Text Preprocessing

- Lowercasing
- Stop-word Removal
- Tokenization
- Hyphen Handling

### Text Normalization

- Stemming
- Lemmatization

### Phrase Query Processing

- Biword Index
- Positional Index

### Index Structures

- Binary Search Tree (BST)
- B-Tree

### Tolerant Retrieval

- K-Gram Indexing
- Edit Distance Matching
- Wildcard Query Processing

---

## Output

The application provides:

- Preprocessed document text
- Stemmed and lemmatized outputs
- Phrase query search results
- Biword Index representation
- Positional Index representation
- BST vs B-Tree performance comparison
- K-Gram Index representation
- Spell correction suggestions
- Wildcard query results
- Experimental observations and conclusions

---

## Author

Information Retrieval System Assignment

Developed using Python, Streamlit, Pandas, NLTK, and NumPy.
