# Heart Attack Predictor

This project is a heart attack prediction web application built using **Logistic Regression**, **Flask**, and **HTML**. The app allows users to input their health data and receive a prediction of their likelihood of having a heart attack, offering valuable insights into heart health.

## Features

- **Logistic Regression Model**: Utilizes logistic regression to predict the probability of a heart attack based on various health metrics.
- **Web Interface**: A simple and intuitive HTML-based user interface to input data and view predictions.
- **Flask Backend**: Connects the frontend with the machine learning model, handles data processing, and returns predictions.

## Parameters Used

The model uses the following health parameters for prediction:

- **male**: Gender of the patient.
- **age**: Age of the patient.
- **education**: Level of education.
- **currentSmoker**: Whether the patient is a current smoker.
- **cigsPerDay**: Number of cigarettes smoked per day.
- **BPMeds**: Whether the patient is on blood pressure medication.
- **prevalentStroke**: History of stroke.
- **prevalentHyp**: History of hypertension.
- **diabetes**: Whether the patient has diabetes.
- **totChol**: Total cholesterol level.
- **sysBP**: Systolic blood pressure.
- **diaBP**: Diastolic blood pressure.
- **BMI**: Body mass index.
- **heartRate**: Maximum heart rate achieved.
- **glucose**: Glucose level.
- **TenYearCHD**: Whether the patient had coronary heart disease within the past 10 years.

## How It Works

1. Users enter their health details into the web form.
2. The app processes these inputs using the logistic regression model to predict the probability of a heart attack.
3. The prediction is displayed on the interface, providing a risk assessment based on the input data.

## Technologies Used

- **Machine Learning**: Logistic Regression for prediction.
- **Web Framework**: Flask for backend development.
- **Frontend**: HTML for creating the user interface.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heart-attack-predictor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd heart-attack-predictor
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to access the web app.

## Usage

- Input your health information in the provided fields.
- Click "Submit" to receive a prediction of your heart attack risk.

## Future Enhancements

- Incorporate additional machine learning models to enhance prediction accuracy.
- Improve data visualization for better risk assessment.
- Add more health parameters to provide a comprehensive analysis.
