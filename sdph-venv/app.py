from flask import Flask, render_template, request, jsonify
from image_processing import upload_and_process_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'D:/Engenharia de Software/Phyton/SDPH/upimages'

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
    
    result = upload_and_process_image(file)

    if 'error' in result:
        error_invalid_file = result['error']
    else:
        success_message = result['message']

    return render_template("processing.html", success_message=success_message, error_invalid_file=error_invalid_file)

if __name__ == '__main__':
    app.run(debug=True)