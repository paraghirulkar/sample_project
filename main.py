#!/usr/bin/env python
# coding: utf-8

#import required libraries
import pandas as pd
import numpy as np
from flask import Flask,request
import pickle 
from sklearn import datasets


#load data set
df = datasets.load_diabetes()

#pick just one feature
X = df['data'][:,np.newaxis,2]


#import linear regression model
from sklearn import linear_model


#create and save the model
regr = linear_model.LinearRegression()


regr.fit(X,df.target)

# create a pickle file to save the model
pickle.dump(regr,open('diabetes.pkl','wb'))


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome diabetes paitents"

@app.route('/prediction',methods=['GET'])
def predict():
    feat = request.args.get('inp_f')
    load_model = pickle.load(open('diabetes.pkl','rb'))
    pred = load_model.predict([[feat]])
    return f"The predicted value is {pred}"

import os 

if __name__ == "__main__":
    app.run()
