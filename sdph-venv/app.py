from flask import Flask, render_template, request, jsonify
from image_handling import upload_image
from werkzeug.utils import secure_filename
from image_processing import process_image_with_face_recognition

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'D:/Engenharia de Software/Phyton/SDPH/sdph-venv/static/upimages'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    success_message = None
    error_invalid_file = None

    if 'file' not in request.files:
        return jsonify({'error': 'no file part'})
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'no selected file'})
    
    result = upload_image(file)

    if 'error' in result:
        error_invalid_file = result['error']
    else:
        image_path = result['image_path']
        filename = secure_filename(file.filename)
        processed_result = process_image_with_face_recognition(image_path, filename)
        if 'error' in processed_result:
            error_invalid_file = processed_result['error']
        else:
            success_message = processed_result['message']
            processed_image_path = processed_result['processed_image_path']
            processed_image_filename = processed_result['processed_image_filename']

    return render_template("processing.html", success_message=success_message, error_invalid_file=error_invalid_file, processed_image_filename=processed_image_filename)

if __name__ == '__main__':
    app.run(debug=True)