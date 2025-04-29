# main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from utils.ocr import extract_text_from_image
from utils.parser import parse_lab_tests

app = FastAPI(
    docs_url="/docs",          # swagger UI
    redoc_url="/redoc",        # ReDoc UI
    openapi_url="/openapi.json" 
)

# simple root so GET / no longer 404
@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Lab-test API is up. POST an image to /get-lab-tests or visit /docs"
    }

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = extract_text_from_image(contents)
        lab_tests = parse_lab_tests(text)
        return JSONResponse({
            "is_success": True,
            "data": lab_tests
        })
    except Exception as e:
        return JSONResponse({
            "is_success": False,
            "data": [],
            "error": str(e)
        }, status_code=500)
