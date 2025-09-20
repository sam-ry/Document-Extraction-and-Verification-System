# utils/extract_pan.py
# PAN-specific field extraction using regex and simple rules
import re

def extract_pan_details(text):
    data = {}
    lines = text.strip().split('\n')

    # PAN Number (5 letters, 4 digits, 1 letter)
    for i, line in enumerate(lines):
        match = re.search(r'\b([A-Z]{5}[0-9]{4}[A-Z])\b', line)
        if match:
            pan_number = match.group(1)
            data['pan_number'] = pan_number
            pan_idx = i
            break

    # Name (usually the first line in most PAN cards)
    name = None
    for line in lines:
        # print(line, lines.index(line), pan_idx)
        if lines.index(line) > pan_idx:  # Ensure name is before PAN number
            if line and not re.search(r'\d', line) and not any(word in line.upper() for word in ['INCOME', 'TAX', 'GOVERNMENT', 'INDIA', 'PERMANENT', 'ACCOUNT', 'NUMBER']):
                name = line.strip()
                break
    if name:
        data['name'] = name

    # DOB
    dob_match = re.search(r'(\d{2}/\d{2}/\d{4})', text)
    if dob_match:
        data['dob'] = dob_match.group(1)

    return data