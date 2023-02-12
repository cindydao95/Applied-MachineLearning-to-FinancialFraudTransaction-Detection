import pickle5 as pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd
from transform_prediction_data import transform_text, transform_input_data, encode_user_data
import json

with open('scale_usd_amount.pkl','rb') as f:
    usd_scale = pickle.load(f)

with open("initial_data.json",'r') as f:
    initial_data = json.load(f) #dict

app = Flask(__name__)
#load the model
with open('logitmodel.pkl','rb') as f:
    logitmodel = pickle.load(f)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    #print(data)
    #transform the raw input data from user
    encoded_data = encode_user_data(transform_input_data(data,scalar=usd_scale),init_data=initial_data) #dictionary

    final_data = np.array(list(encoded_data.values())).reshape(1,-1) #ready data for prediction

    output = logitmodel.predict(final_data)
    #print(output[0])
    if output[0] == 1:
        result = "Fraud"
    else:
        result = "Non-Fraud"
    return jsonify(result)

@app.route('/predict',methods = ['POST'])
def predict():
    data = request.form

    encoded_data = encode_user_data(transform_input_data(data,scalar=usd_scale),init_data=initial_data) #dictionary

    final_data = np.array(list(encoded_data.values())).reshape(1,-1) #ready data for prediction
    output = logitmodel.predict(final_data)
    
    if output[0] == 1:
        output = "Fraud"
    else:
        output = "Non-Fraud"
    return render_template("home.html",prediction_text=f"{output}")
if __name__ == "__main__":
    app.run(debug=True)

    
    


