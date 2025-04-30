from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    height = float(request.form['height'])
    prediction = model.predict(np.array([[height]]))
    weight = round(prediction[0], 2)
    return render_template('results.html', height=height, weight=weight)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
