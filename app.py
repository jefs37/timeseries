from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

df = pd.read_csv('searches.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/timeseries')
def timeseries():
    return render_template('timeseries.html')

@app.route('/predictions', methods = ['POST', 'GET'])
def predictions():
    if request.method == 'POST':
        return render_template('predictions.html')
    return render_template('predictions.html')

if __name__ == "__main__":
    app.run(debug=True)