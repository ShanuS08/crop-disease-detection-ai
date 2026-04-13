from flask import Flask, render_template, request
import os

from utils.image_predict import load_image_model, predict_image
from utils.text_model import predict_text

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

load_image_model()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    image_result = ("No Image", 0)
    text_result = ("No Text", 0)

    # IMAGE
    if 'image' in request.files:
        file = request.files['image']
        if file and file.filename != "":
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            image_result = predict_image(filepath)

    # TEXT
    text_input = request.form.get('text')
    if text_input:
        text_result = predict_text(text_input)

    # FINAL DECISION
    final_result = image_result if image_result[1] > text_result[1] else text_result

    # ✅ ALWAYS RETURN (VERY IMPORTANT)
    return render_template(
        'index.html',
        image_result=image_result,
        text_result=text_result,
        final_result=final_result
    )
    
if __name__ == '__main__':
    app.run(debug=True)


