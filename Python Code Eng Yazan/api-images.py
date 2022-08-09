import os
from flask import Flask,  request
import numpy as np
from PIL import Image
import cv2

app = Flask(__name__)
APP_ROUTE = os.path.dirname(os.path.abspath(__file__))

@app.route("/get_image", methods = ['POST'])
def get_image():
    file = request.files["image"]
    img = Image.open(file.stream)
    img = np.asarray(img)
    cv2.imwrite('output.jpg', img)
    1) pre process
    2) model.predict(img)
    return answer


if __name__ == "__main__":
    app.run( debug=False, host= '0.0.0.0', port= 5000)