from PIL import Image
from pytesseract import *

filename = "C:\\Users\\jin\\Desktop\\playdata\\video\\p0624\\img\\tesseract_test.jpg"
image = Image.open(filename)
text = image_to_string(image, lang="eng")
print(text)