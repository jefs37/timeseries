from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

df = pd.read_csv('searches.csv')

print(df.head())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/predictions')
def predictions():
    return render_template('predictions.html')

if __name__ == "__main__":
    app.run(debug=True)