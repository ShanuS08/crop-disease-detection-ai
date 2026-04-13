import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = None

# IMPORTANT: match your training folders
class_names = [
    "apple_scab",
    "healthy",
    "potato_blight",
    "tomato_blight"
]

def load_image_model():
    global model
    try:
        model = load_model('model/image_model.h5')
        print("✅ Model loaded successfully")
    except Exception as e:
        print("❌ Error loading model:", e)
        model = None

def predict_image(img_path):
    if model is None:
        return "Model not loaded", 0

    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]

    return predicted_class, 1
