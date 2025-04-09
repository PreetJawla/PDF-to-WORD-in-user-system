from flask import Flask, render_template, request, send_file
from pdf2docx import Converter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'converted_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_pdf():
    if 'pdf_file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['pdf_file']
    if file.filename == '':
        return 'No selected file', 400

    filename = secure_filename(file.filename)
    pdf_path = os.path.join(UPLOAD_FOLDER, filename)
    docx_filename = filename.rsplit('.', 1)[0] + '.docx'
    docx_path = os.path.join(UPLOAD_FOLDER, docx_filename)

    file.save(pdf_path)

    # Convert PDF to DOCX
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

    return send_file(docx_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
