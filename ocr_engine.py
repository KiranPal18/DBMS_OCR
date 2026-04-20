from paddleocr import PaddleOCR
import os

# Skip connectivity checks to start faster
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"

# Initialize with GPU
try:
    # use_angle_cls=True here is enough to enable orientation correction
    ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True)
except ValueError:
    ocr = PaddleOCR(use_angle_cls=True, lang='en', device='gpu')

def extract_text(file_path: str) -> str:
    # REMOVED: cls=True from the call below
    result = ocr.ocr(file_path) 
    
    full_text = []
    if result:
        for page in result:
            if page:
                for line in page:
                    # line[1][0] is the recognized text
                    full_text.append(line[1][0])
    
    return " ".join(full_text)