import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from cnnClassifier.pipeline.prediction import Predictionpipeline
from cnnClassifier.utils.common import decodeImage

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "InputImage.jpeg"
        self.classifier = Predictionpipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET'])
@cross_origin()
def train_route():
    os.system("dvc repro")
    return "Training done successfully"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predict_route():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8888)
