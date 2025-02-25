import os
from flask import Flask, render_template, request
import joblib

heart = Flask(__name__)

# Get the absolute path of the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the model file (assuming it's in the same directory as heart.py)
model_file_path = os.path.join(BASE_DIR, 'heart_disease_prediction.pkl')

# Load the trained model
try:
    model = joblib.load(model_file_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Model file not found at {model_file_path}. Ensure it's in the same directory.")

@heart.route('/')
def home():
    return render_template('index.html')

@heart.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from form
        age = int(request.form.get('age'))
        sex = int(request.form.get('sex'))
        cp = int(request.form.get('cp'))
        trestbps = int(request.form.get('trestbps'))
        chol = int(request.form.get('chol'))
        fbs = int(request.form.get('fbs'))
        restecg = int(request.form.get('restecg'))
        thalach = int(request.form.get('thalach'))
        exang = int(request.form.get('exang'))
        oldpeak = float(request.form.get('oldpeak'))
        slope = int(request.form.get('slope'))
        ca = int(request.form.get('ca'))
        thal = int(request.form.get('thal'))
    
        # Prepare data for model prediction
        input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        prediction = model.predict(input_data)

        # Determine result message
        result = "You have heart disease." if prediction[0] == 1 else "You don't have heart disease."

        return render_template('result.html', result=result)

    except Exception as e:
        return f"Error in prediction: {e}"

if __name__ == '__main__':
    heart.run(debug=True)
