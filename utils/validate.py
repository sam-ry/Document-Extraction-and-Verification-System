# app/utils/validate.py
# Format validation and masking detection

import re

MASK_PATTERNS = [r"X{3,}", r"\*{3,}"]

def validate_format(id_number: str, regex_pattern: str) -> bool:
    if not id_number:
        return False
    return bool(re.fullmatch(regex_pattern, id_number))

def detect_masking(text: str) -> bool:
    for pattern in MASK_PATTERNS:
        if re.search(pattern, text):
            return True
    return False
