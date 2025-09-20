# app/services/verification.py
# Orchestrator for verification pipeline

from app.utils.ocr import extract_text_from_image
from app.utils.classify import classify_document
from app.utils.extract import extract_fields, PAN_REGEX, AADHAAR_REGEX, PASSPORT_REGEX, DL_REGEX
from app.utils.validate import validate_format, detect_masking
from app.utils.schema import DocumentResultSchema
from app.utils.extract_pan import extract_pan_details
from app.utils.extract_aadhar import extract_aadhar_details

def verify_document(file_path: str, file_type: str = "image") -> dict:
    # Step 1: OCR
    # if file_type == "pdf":
    #     text = extract_text_from_pdf(file_path)
    # else:
    text = extract_text_from_image(file_path)

    # Step 3: Classify
    doc_type = classify_document(text)

    # Step 4: Extract fields
    EXTRACTION_FUNCTIONS = {
    "PAN": extract_pan_details,
    "AADHAAR": extract_aadhar_details
    }
    extractor = EXTRACTION_FUNCTIONS.get(doc_type)
    fields = extractor(text) if extractor else {}

    # Step 5: Validation and masking
    masked = detect_masking(text)

    regex_map = {
        "PAN": PAN_REGEX,
        "AADHAAR": AADHAAR_REGEX
        # "PASSPORT": PASSPORT_REGEX,
        # "DL": DL_REGEX
    }
    format_valid = False
    if "id_number" in fields and doc_type in regex_map:
        format_valid = validate_format(fields["id_number"], regex_map[doc_type])

    return {
        "document_type": doc_type,
        "extracted_fields": fields,
        "format_valid": format_valid,
        "masked": masked,
        "fraud_detected": False  # Placeholder for future fraud detection logic
    }