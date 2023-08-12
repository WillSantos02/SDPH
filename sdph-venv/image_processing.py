import os
import cv2
from flask import current_app

def process_image_with_face_recognition(image_path, filename):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    frame = cv2.imread(image_path)

    if frame is None:
        print("Erro ao carregar a imagem")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    processed_image_filename = 'processed_' + filename
    processed_image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], processed_image_filename)
    cv2.imwrite(processed_image_path, frame)

    return {'message': 'Image processed successfully!', 'processed_image_path': processed_image_path, 'processed_image_filename':processed_image_filename}