import pytesseract
from PIL import Image
import io

# ← add this line pointing to your install location:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("L")
    text  = pytesseract.image_to_string(image)
    return text
