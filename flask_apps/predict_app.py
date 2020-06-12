import base64
import numpy as np
import io
from PIL import Image
"""
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from tensorflow.keras.optimizers import Adam
"""
import tensorflow as tf

import keras
from keras import backend as K
from keras.backend import set_session
from keras.models import Sequential
from keras.models import load_model
from keras.layers.core import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array

from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

sess = tf.Session()
graph = tf.get_default_graph()

def get_model():
    global model,sess
    set_session(sess)
    model_path = 'VGG16_bikes_cars_trains_rollers_trucks.h5'
    vgg16_model = keras.applications.vgg16.VGG16()
    model = Sequential()
    for layer in vgg16_model.layers[:-1]:
        model.add(layer)
    for layer in model.layers:
        layer.trainable = False
    model.add(Dense(5, activation='softmax'))
    model.load_weights(model_path)
    model._make_predict_function()#
    #model = load_model('VGG16_cats_and_dogs.h5')
    print(" * Model loaded!")

def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

print(" * Loading Keras model...")
get_model()


@app.route("/predict", methods=["POST"])
def predict():
    global graph, model, sess
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))
    
    #model.predict(None) 
    with graph.as_default():
        set_session(sess)
        prediction = model.predict(processed_image).tolist()
    
    response = {
        'prediction': {
            'bicycles': prediction[0][0],
            'cars': prediction[0][1],
            'trains': prediction[0][2],
            'roller_blades': prediction[0][3],
            'trucks': prediction[0][4],
        }
    }
    return jsonify(response)