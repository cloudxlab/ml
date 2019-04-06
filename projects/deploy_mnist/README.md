The purpose of this project is to show how to move your machine learning models in production. In this project, we'll train the MNIST model, save the model to the file, load the model from the file in the flask app and predict the digit for the new images. Since input images in MNIST are 28x28 greyscale images, the images used for predictions have to be processed. They should be converted to greyscale and resized to 28x28 pixels. Because of this you may not get the accuracy in predictions but you will learn how to move your model to production (and this is the sole objective of this project).

We'll use Flask for exposing the model using the REST API for predictions. Flask is a micro web framework written in Python. It's light weight and easy to learn.

# Steps

## Clone to repository
```
git clone https://github.com/cloudxlab/ml.git
```

## Create virtual environment

```
cd ml/projects/deploy_mnist/
virtualenv -p python3 venv
```

## Activate virtual environment

```
source venv/bin/activate
```

## Install the flask and other requirements
```
pip install -r requirements.txt
```

## Train the model

The trained model will be saved in trained_models directory
```
mkdir -p trained_models
python train_mnist_model.py
```

## Start the flask server for predictions

For the API code, see the file `predictions.py` under `flask_app` directory. Run the server on port 4041. If the port is already in use then use any of the port in the range of 4040 to 4060 as on CloudxLab only these ports are open for public access.

```
cd flask_app
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
export FLASK_APP=predictions.py
flask run --host 0.0.0.0 --port 4041
```

## Predict the digit for the new image

We will use the test images for predictions. Login to another console and run below commands.
```
cd ml/projects/deploy_mnist/
curl -F 'file=@test-images/7.png' 127.0.0.1:4041/predict
```

The REST API will return something like below JSON object

```{"digit":7}```

## Public API

Your server is running on 0.0.0.0 and say your web console is on e.cloudxlab.com then you can use this REST API for your usages http://e.cloudxlab.com:4041/predict

Replace 4041 with the port number on which your server is running.

## Next Steps

The above flask server runs in the development mode. For production usage, you would like to run the server using Nginx and uWSGI. For details please follow this documentation http://flask.pocoo.org/docs/1.0/deploying/
