from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

model = load_model('model_filter.h5')

label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def preprocess_image(image_path):
    img = image.load_img(image_path, grayscale=True, target_size=(48, 48))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255
    return x

def create_uploads_folder():
    uploads_folder = 'uploads'
    if not os.path.exists(uploads_folder):
        os.makedirs(uploads_folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    create_uploads_folder()  # Ensure 'uploads' folder exists

    if file:
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        processed_image = preprocess_image(file_path)
        predictions = model.predict(processed_image)

        emotion_index = np.argmax(predictions)
        predicted_emotion = label_map[emotion_index]

        return jsonify({'predicted_emotion': predicted_emotion})

if __name__ == '__main__':
    app.run(debug=True)
