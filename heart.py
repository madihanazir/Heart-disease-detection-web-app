import os

# Get the absolute path to the model file
model_file_path = os.path.join(os.path.dirname(__file__), 'C:/Users/Madiha/Documents/flaskheart/venv/heart_disease_prediction.pkl')




from flask import Flask, render_template, request
import joblib

heart = Flask(__name__)

# Load the trained model
model = joblib.load(model_file_path)

@heart.route('/')
def home():
    return render_template('index.html')

@heart.route('/predict', methods=['GET', 'POST'])
def predict():

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
  
    result = ""
    # Make a prediction using the loaded model
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = model.predict(input_data)

    # Display the prediction result
    if prediction[0] == 1:
        result = "You have heart disease."
    else:
        result = "You don't have heart disease."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    heart.run(debug=True)
