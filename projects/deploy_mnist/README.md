# The purpose of this project is to show how to move your machine learning models in production. We'll train the MNIST model, save the model to the file, load the model from the file in the flask app and predict the results for the new image. Since input images in MNIST are 28x28 greyscale images, the images used for predictions have to be processed. They should be converted to greyscale and resized to 28x28 pixels. You may not get the accuracy in predictions but you will learn how can you move your model to production.

## Create virtual environment

virtualenv -p python3 venv

## Activate virtual environment

source venv/bin/activate

## Install the flask and other requirements

pip install -r requirements.txt

## Train the model

### The trained model will be saved in trained_models directory

python train_mnist_model.py

## Start the flask server for predictions

### The server runs on port 4041. If the port is already in use then use any of the port in the range of 4040 to 4060

cd flask_app
export FLASK_APP=predictions.py
flask run --host 0.0.0.0 --port 4041


## Test the code

curl -F 'file=@test-images/7.png' 127.0.0.1:4041/predict
