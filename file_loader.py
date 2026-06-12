def load_uploaded_files(uploaded_files):
    """
    Convert uploaded text files into a dictionary.

    Returns:
    {
        "doc1.txt": "text content",
        "doc2.txt": "text content"
    }
    """

    documents = {}

    for file in uploaded_files:

        text = file.read().decode("utf-8")

        documents[file.name] = text

    return documents