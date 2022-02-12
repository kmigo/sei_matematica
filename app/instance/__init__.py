
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


def create_app():
    @app.route('/')
    def home():
        from PIL import Image
        import pytesseract
        import os 
       
        
        dirs = os.listdir()
        try:
            res = pytesseract.image_to_string( Image.open('imagem-teste-com-ocr.jpeg'), lang='por')
            return str(res)
        except Exception as e:
            return str(e)    
    return app

