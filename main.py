# app/main.py
# FastAPI entry point for verifying uploaded documents

# py -3.13 -m uvicorn app.main:app --reload

from fastapi import FastAPI, UploadFile, File
import shutil
import os
from app.services.verification import verify_document
from paddleocr import PaddleOCR

app = FastAPI()  # Create the FastAPI app

UPLOAD_DIR = "uploads"  # Folder where uploaded files will be saved
os.makedirs(UPLOAD_DIR, exist_ok=True)

from pymongo import MongoClient

# Create a MongoDB client (reuse this if possible)
client = MongoClient("mongodb://localhost:27017")

# Access your database and collection
db = client["id_data"]
collection = db["documents"]

# Define a POST endpoint at /verify
@app.post("/verify")
async def verify(file: UploadFile = File(...)):
    # Build full path to save the uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  # Copy file content into saved file

    ext = file.filename.split(".")[-1].lower()
    file_type = "pdf" if ext == "pdf" else "image"

    result = verify_document(file_path, file_type)

    insert_result = collection.insert_one(result)

    # MongoDB adds '_id' ObjectId to result dict, so fetch it:
    result["_id"] = str(insert_result.inserted_id)  # Convert ObjectId to string for JSON
    return result