from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

# Home route to render input form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from form input
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # Make prediction
    prediction = model.predict(final_features)
    
    output = 'Yes' if prediction[0] == 1 else 'No'
    
    return render_template('index.html', prediction_text=f'Customer will churn: {output}')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
