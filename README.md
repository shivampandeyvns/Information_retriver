# Information Retrieval System

## Overview

This project implements a complete Information Retrieval (IR) System using Python and Streamlit. The application demonstrates various indexing and retrieval techniques including:

- Text Preprocessing
- Stemming vs Lemmatization
- Inverted Index Construction
- Phrase Query Processing (Biword Index and Positional Index)
- BST vs B-Tree Performance Comparison
- Tolerant Retrieval using K-Gram Index
- Edit Distance Based Spell Correction
- Wildcard Query Processing

---

## Prerequisites

Ensure that Python 3.9 or later is installed on your system.

Verify installation:

bash python --version 

---

## Required Libraries

Install the required libraries using:

bash pip install -r requirements.txt 

Alternatively, install them individually:

bash pip install streamlit pip install pandas pip install nltk pip install bintrees 

---

## Project Structure

```text
project/
│
├── app.py
├── preprocessing.py
├── phrase_query.py
├── tolerant_retrieval.py
├── btree_index.py
├── evaluation.py
├── requirements.txt
└── sample_documents/
    ├── doc1.txt
    ├── doc2.txt
    ├── doc3.txt
    ├── doc4.txt
    ├── doc5.txt
    ├── doc6.txt
    └── doc7.txt
```

---

## Running the Application

### Option 1: Use the Deployed Application

Access the live application directly: https://bits-assignment-ir.streamlit.app/

### Option 2: Run Locally

Navigate to the project directory and execute the below code in a terminal:

```
streamlit run app.py
```

The application will launch in the default browser at:

```
http://localhost:8501
```
---

## How to Use the Application

### Step 1: Upload Documents

- Open the Documents tab.
- Upload one or more text (.txt) files.
- Verify that the uploaded documents are displayed correctly.

### Step 2: Preprocessing

- Navigate to the Preprocessing tab.
- Review the cleaned and normalized document text.

### Step 3: Stemming vs Lemmatization

- Open the Stem vs Lemma tab.
- Compare the outputs produced by stemming and lemmatization.

### Step 4: Inverted Index

- Open the Inverted Index tab.
- View the generated term-document mappings.

### Step 5: Phrase Query Processing

- Open the Phrase Query tab.
- Enter phrase queries such as:

text machine learning artificial intelligence 

- Compare the results produced by:
  - Biword Index
  - Positional Index

### Step 6: BST vs B-Tree Comparison

- Open the BST vs BTree tab.
- Review search results and execution times for both indexing structures.

### Step 7: Tolerant Retrieval

- Open the Tolerant Retrieval tab.

Examples:

Misspelled Query:

text machian 

Wildcard Query:

text mach* 

- Observe spell correction suggestions, edit distance values, and wildcard matches.

### Step 8: Inference

- Open the Inference tab.
- Review observations and conclusions derived from the experimental results.

---

## Output

The application provides:

- Preprocessed document text
- Stemmed and lemmatized terms
- Inverted index representation
- Phrase query results
- BST vs B-Tree performance comparison
- K-Gram index representation
- Spell correction suggestions
- Wildcard query results
- Experimental observations and inferences

---

## Authors

Shivam Pandey, Saurav Sinha, Rahul Chauhan

Developed using Python, NLTK, Pandas, and Streamlit.
