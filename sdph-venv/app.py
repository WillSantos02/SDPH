from flask import Flask, render_template, request, jsonify
from image_processing import upload_and_process_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'D:/Engenharia de Software/Phyton/SDPH/upimages'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'no file part'})
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'no selected file'})
    
    result = upload_and_process_image(file)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)