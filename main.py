import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

    img = cv2.imread('imgs/rg.png')

    result = pytesseract.image_to_string(img)

print(result)