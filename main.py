import os
import shutil
import json
import time
from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv
from google import genai
from pydantic import ValidationError

# Local imports
from schema import CompanyDetails

load_dotenv()

app = FastAPI(title="Placement Brochure Auto-Fill (Fixed)")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.post("/upload-brochure")
async def process_document(file: UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # 1. Upload file to llama (FIXED KEYWORD)
        print(f"--- Uploading {file.filename} ---")
        uploaded_file = client.files.upload(file=temp_file)

        # 2. Wait for file processing (Standard for 2026 Multimodal)
        while uploaded_file.state.name == "PROCESSING":
            print("Waiting for llama to process the document...")
            time.sleep(2)
            uploaded_file = client.files.get(name=uploaded_file.name)
        
        if uploaded_file.state.name == "FAILED":
            raise Exception("llama file processing failed.")

        # 3. Prompting llama 3.1 Flash Lite
        prompt = f"""
        Extract company and internship details from this brochure.
        
        ISM DHANBAD MAPPING:
        - MnC/MNC -> Mathematics & Computing
        - EE -> Electrical Engineering
        - ECE -> Electronics & Communication Engineering
        
        Return ONLY valid JSON.
        """

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=[uploaded_file, prompt],
            config={
                "response_mime_type": "application/json",
                "response_json_schema": CompanyDetails.model_json_schema(),
            }
        )

        # 4. Cleanup
        os.remove(temp_file)
        
        return json.loads(response.text)

    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)