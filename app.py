from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__ , static_url_path ="/static")

# Load your trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input values from the form
        age = int(request.form['age'])
        sex_male = 1 if request.form['sex'] == 'male' else 0  # Convert gender to numeric
        cigs_per_day = int(request.form['cigsPerDay'])
        tot_chol = float(request.form['totChol'])
        sys_bp = float(request.form['sysBP'])
        glucose = float(request.form['glucose'])
        
        # Create input array for prediction
        input_data = np.array([[age, sex_male, cigs_per_day, tot_chol, sys_bp, glucose]])
        
        # Perform prediction
        prediction = model.predict(input_data)
        if prediction ==1:
            result = "You Are Vulnerable"
        elif prediction ==0:
            result = "You Are Safe"

        # Return the predicted value
        return render_template('result.html', prediction=result)
        

if __name__ == '__main__':
    app.run(debug=True)
