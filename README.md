# Heart Disease Prediction Web App

This is a Flask-based web application for predicting heart disease using a trained machine learning model.

## 🚀 Features
- User-friendly form for inputting patient details
- Predicts heart disease risk based on input features
- Minimalistic and responsive UI
- Deployed using Flask

## 📂 Project Structure
```
📁 project-root
├── heart.py               # Flask application
├── heart_disease_prediction.pkl  # Trained ML model
├── templates
│   ├── index.html         # Input form
│   ├── result.html        # Prediction result page
├── static
│   ├── style.css          # Stylesheet (if applicable)
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

## ⚡ Getting Started

### Prerequisites
Ensure you have Python 3 installed and the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
python heart.py
```
The app will be available at `http://127.0.0.1:5000/`

### Deployment
To deploy on a cloud platform (e.g., Heroku, Render):
1. Ensure `requirements.txt` is up to date:
   ```bash
   pip freeze > requirements.txt
   ```
2. Use a `Procfile` if deploying on Heroku:
   ```
   web: gunicorn heart:app
   ```
3. Deploy using platform-specific instructions.

## 🛠 API Endpoints
- `/` - Home page with input form
- `/predict` - Handles form submission and returns prediction results


## ✨ Acknowledgments
- Machine learning model trained on publicly available datasets
- Flask for web framework



