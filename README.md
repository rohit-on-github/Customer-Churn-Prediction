# Customer Churn Prediction

This project predicts whether a customer will churn (leave the service) using machine learning techniques. It involves building a model, evaluating its performance, and deploying it via a web app built with Flask.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Dataset](#dataset)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project is structured as an end-to-end machine learning solution for predicting customer churn. It covers:
- **Data Preprocessing**: Cleaning and preparing the data for analysis.
- **Model Building**: Training a machine learning model (Random Forest Classifier).
- **Model Deployment**: Deploying the trained model through a Flask web app that allows users to make predictions using a simple interface.

## Technologies Used

- **Python**: Core programming language used for the project.
- **Pandas**: Used for data manipulation and preprocessing.
- **Scikit-learn**: For building and training the machine learning model.
- **Flask**: Used to create the web app for deploying the model.
- **HTML/CSS**: For building the front-end user interface.
- **Pickle**: For saving and loading the trained model.

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/customer_churn_prediction.git
cd customer_churn_prediction
```

### 2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. (Optional) Train the model:
You can retrain the model by running the Jupyter Notebook `churn_model.ipynb` which will generate a new `model.pkl` file.

### 4. Run the Flask app:

```bash
python app.py
```

This will start the web server locally, and you can access the app by opening `http://127.0.0.1:5000/` in your browser.

## How to Use

1. Run the Flask app as described in the installation steps.
2. Input the required customer data into the web form.
3. Click on "Predict" to see whether the customer is likely to churn.

## Dataset

This project uses the [Telco Customer Churn Dataset](https://raw.githubusercontent.com/IBM/customer-churn-prediction/master/WA_Fn-UseC_-Telco-Customer-Churn.csv) which contains data about customer demographics, services, and contracts.

Key features include:
- `tenure`: Number of months the customer has stayed with the company.
- `MonthlyCharges`: The amount billed to the customer monthly.
- `TotalCharges`: Total amount billed to the customer.
- `Churn`: Whether the customer has churned (Yes or No).

## Results

The Random Forest Classifier model achieved an accuracy of **~80%** on the test set. This provides a reasonable baseline for predicting customer churn.

## Future Work

- **Model Tuning**: Improve model performance by tuning hyperparameters.
- **Cloud Deployment**: Deploy the Flask app on a cloud platform like **Microsoft Azure** or **Heroku** for public access.
- **Additional Models**: Experiment with other machine learning models like XGBoost, LightGBM, or neural networks.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
