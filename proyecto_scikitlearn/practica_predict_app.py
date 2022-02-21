import pickle
import pandas as pd

from flask import Flask, jsonify, request

from practica_predict_services import predict_single

app = Flask('practica-predict')

with open('models/practica_model.pck', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    customer = pd.DataFrame(request.get_json())
    prediction = predict_single(customer, model)
    result = {
        'converted': bool(prediction)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)