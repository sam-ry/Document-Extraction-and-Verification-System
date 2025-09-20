# utils/extract_aadhar.py
# Aadhar-specific field extraction using regex and simple rules
import re

def extract_aadhar_details(text):
    data = {}

    # aadhar Number (12 digits, possibly spaced)
    aadhar_number = re.search(r'(\n\d{4}\s\d{4}\s\d{4})', text)
    if aadhar_number:
        data['aadhar_number'] = aadhar_number.group(1)[1:]

    # Name (First line in most cards)
    lines = text.strip().split('\n')
    # print('lines:', lines)
    name = None
    for line in lines:
        # exclude known keywords and lines with digits
        if line and not re.search(r'\d', line) and not any(word in line.upper() for word in ['GOVERNMENT', 'INDIA', 'DOB', 'FEMALE', 'MALE', 'MOBILE', 'VID']):
            name = line.strip()
            break
    if name:
        data['name'] = name

    # Gender
    male = re.search(r'male', text, re.IGNORECASE)
    female = re.search(r'female', text, re.IGNORECASE)
    if male:
        data['gender'] = 'Male'
    elif female:
        data['gender'] = 'Female'

    # DOB or YOB
    dob_match = re.search(r'(\d{2}/\d{2}/\d{4})', text)
    yob_match = re.search(r'Year of Birth\s*:?(\d{4})', text)
    if dob_match:
        data['dob'] = dob_match.group(1)
    elif yob_match:
        data['yob'] = yob_match.group(1)

    return data