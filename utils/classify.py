# app/utils/classify.py
# Rule-based document classification

CLASSIFICATION_RULES = {
    "PAN": ["income", "tax", "department", "permanent account number"],
    "AADHAAR": ["government", "of", "india", "aadhaar"]
    # "DL": ["driving licence", "transport department"],
    # "PASSPORT": ["republic of india", "passport"],
    # "VOTER": ["election commission of india"],
    # "MARKSHEET": ["marksheet", "secondary school"]
}

def classify_document(text: str):
    text = text.lower()  # make search case-insensitive
    for doc_type, keywords in CLASSIFICATION_RULES.items():
        for keyword in keywords:
            if keyword in text:
                return doc_type # return immediately when first keyword is found
    return None  # if nothing matched

if __name__ == "__main__":
    sample_text = """
    income of India
    This is to certify that the holder of this number is a resident of India.
    """
    doc_type = classify_document(sample_text.lower())
    print(f"Document Type: {doc_type}")