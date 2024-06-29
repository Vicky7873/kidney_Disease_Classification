import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,img_to_array
import numpy as np


class Predictionpipeline:
    def __init__(self,filename):
        self.filename = filename

    def predict(self):
        model = load_model('artifacts/training/model.h5')
        img = image.load_img(self.filename, target_size=(224, 224))
        test_img = image.img_to_array(img)
        test_img = np.expand_dims(test_img, axis=0)
        result = np.argmax(model.predict(test_img), axis=1)
        print(result)

        if result[0] == 0:
            prediction = 'Normal'
            return [{ "image" : prediction}]
        else:
            prediction = "Tumor"
            return [{ "image" : prediction}]

