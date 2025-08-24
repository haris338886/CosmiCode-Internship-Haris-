import os
import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Initialize Flask app
app = Flask(__name__)

# Load trained model
MODEL_PATH = 'model/model.h5'
model = load_model(MODEL_PATH)

# Class labels
CLASS_LABELS = ['Cat', 'Dog']

# Predict function
def predict_img(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0

    preds = model.predict(x)
    predicted_class = CLASS_LABELS[np.argmax(preds)]
    confidence = round(100 * np.max(preds), 2)
    return predicted_class, confidence

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join("static", file.filename)
            file.save(file_path)

            pred, confidence = predict_img(file_path)
            return render_template('result.html', file_path=file_path, prediction=pred, confidence=confidence)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
