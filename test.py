from preprocessing import preprocess_document

sample_text = """
Machine-Learning is one of the most exciting
fields of Artificial Intelligence.
"""

result = preprocess_document(
    sample_text,
    method="lemmatization"
)

for key, value in result.items():
    print("\n")
    print(key)
    print(value)