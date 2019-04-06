import numpy as np
from sklearn.externals import joblib
from PIL import Image
from flask import Flask, jsonify, request


app = Flask(__name__)

my_model_loaded = joblib.load("../trained_models/mnist_model.pkl")

@app.route('/predict', methods=["POST"])
def hello_world():
    requested_img = request.files['file']
    greyscale_img = Image.open(requested_img).convert('L')
    resized_image = greyscale_img.resize((28,28))
    img = np.asarray(resized_image)
    img = img.reshape(784,)

    pred = my_model_loaded.predict(img.reshape(1, -1))
    result = int(pred.tolist()[0])
    return jsonify({"digit": result})
