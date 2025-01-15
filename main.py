#import easyocr
#reader = easyocr.Reader(['en'])
#result = reader.readtext('screenshot2.jpg',detail=0)
#output="".join(result)
#print(result)

from pytesseract import pytesseract


class Text_extract:
   def __init__(self):
        self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

   def extract(self, filename):
        try:
            pytesseract.tesseract_cwd = self.path
            text = pytesseract.image_to_string(filename)
            return text
        except Exception as e:
            print(e)
            return "Error"


text_extract= Text_extract()
text = text_extract.extract("F:\Python\Textextract\screenshot.png")
print(text)
