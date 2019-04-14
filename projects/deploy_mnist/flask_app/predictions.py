import numpy as np
from sklearn.externals import joblib
from PIL import Image
from flask import Flask, jsonify, request

# Create flask app
app = Flask(__name__)

# Load the previously trained model from the file
model = joblib.load("../trained_models/mnist_model.pkl")

# /predict is the end point
@app.route('/predict', methods=["POST"])
def predict_image():

    # Read the image uploaded by the curl command
    requested_img = request.files['file']

    '''
    Convert the uploaded image to greyscale.
    Since in MNIST the training images are greyscaled hence we will have to convert the uploaded image to greyscale
    '''
    greyscale_img = Image.open(requested_img).convert('L')

    '''
    Resize the uploaded image to 28x28 pixels.
    Since in MNIST the training images are of 28x28 pixels hence we will have to resize the uploaded image to 28x28 pixels.
    '''
    resized_image = greyscale_img.resize((28,28))

    # Convert the image to an array
    img = np.asarray(resized_image)

    # Reshape the image to (784, 1)
    img = img.reshape(784,)

    # Predict the digit using the trained model
    pred = model.predict(img.reshape(1, -1))

    # Get the digit
    result = int(pred.tolist()[0])

    # Return the JSON response
    return jsonify({"digit": result})
