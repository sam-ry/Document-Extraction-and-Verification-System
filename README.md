# Document-Extraction-and-Verification-System
> A simple OCR-based Aadhaar and PAN card document verification tool with automatic data extraction, validation, MongoDB storage, and a Gradio frontend.

---

## Features

*  Upload image of an Aadhaar or a PAN card
*  OCR text extraction using PaddleOCR
*  Auto document type classification (PAN / Aadhaar)
*  Field extraction (Name, DOB, ID Number, etc.)
*  Format validation using regex
*  Masking detection (for privacy-masked documents)
*  Automatically stores result in MongoDB
*  Gradio frontend for user uploads and result viewing
*  FastAPI backend with `/verify` API endpoint

---

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/sam-ry/Document-Extraction-and-Verification-System.git
cd Document-Extraction-and-Verification-System

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # On Windows

### 3. Install Requirements
pip install -r requirements.txt

Run the Application
Step 1: Start FastAPI Backend (port 8000)
uvicorn app.main:app --reload

You can now POST files to:
http://localhost:8000/verify via Postman

Step 2: Run Gradio Frontend (opens in browser)
python app/gradio_app.py

### 4. Install and run MongoDB locally

* Install [MongoDB Community Edition](https://www.mongodb.com/try/download/community)
* Ensure the MongoDB daemon is running on default port `27017`
* Open MongoDB Compass (GUI) to visualize inserted data (connect to: `mongodb://localhost:27017`)
* Your DB will be: `id_data` and collection: `documents`

---
## How It Works

* User uploads an image via UI or API.
* OCR extracts raw text using PaddleOCR.
* Document type is classified.
* Relevant fields are extracted using custom parsers.
* Format validation is applied using regex.
* Masking check flags sensitive redactions.
* Final result is returned and stored in MongoDB.
