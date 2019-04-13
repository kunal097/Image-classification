from keras.models import model_from_json
from keras_preprocessing import image
import numpy as np
from keras import backend as K





class Classifier:


    def __init__(self):
        json_file = open('model/model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights("model/model.h5")

    def classify(self,file):
        test_image =image.load_img('uploads/'+file, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = self.model.predict(test_image)
        K.clear_session()

        if result[0][0] == 1:
            prediction = 'dog'
        else:
            prediction = 'cat'

        return prediction


