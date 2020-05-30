# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:34:15 2020

@author: Welcome
"""







from flask import Flask,render_template,request


import pickle
import numpy as np


model = pickle.load(open("clf.pkl","rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("project.html")


@app.route('/login',methods =['POST'])
def login():
    Time = request.form['Time']
    V1 = request.form['V1']
    V2 = request.form['V2']
    V3 = request.form['V3']
    V4 = request.form['V4']
    V5 = request.form['V5']
    V6 = request.form['V6']
    V7 = request.form['V7']
    V8 = request.form['V8']
    V9 = request.form['V9']
    V10 = request.form['V10']
    V11 = request.form['V11']
    V12 = request.form['V12']
    V13 = request.form['V13']
    V14 = request.form['V14']
    V15 = request.form['V15']
    V16 = request.form['V16']
    V17 = request.form['V17']
    V18 = request.form['V18']
    V19 = request.form['V19']
    V20 = request.form['V20']
    V21 = request.form['V21']
    V22 = request.form['V22']
    V23 = request.form['V23']
    V24 = request.form['V24']
    V25 = request.form['V25']
    V26 = request.form['V26']
    V27 = request.form['V27']
    V28 = request.form['V28']
    Amount = request.form['Amount']
    
    total=[[float(Time),float(V1),float(V2),float(V3),float(V4),float(V5),float(V6),float(V7),float(V8),float(V9),float(V10),float(V11),float(V12),float(V13),float(V14),float(V15),float(V16),float(V17),float(V18),float(V19),float(V20),float(V21),float(V22),float(V23),float(V24),float(V25),float(V26),float(V27),float(V28),float(Amount)]]
    
    print(total)
    
    preds = model.predict(total)
    
    print(preds)
    
   
    return render_template("project.html", showcase = preds)
    

if __name__ == '__main__':
    app.run(debug = True)

