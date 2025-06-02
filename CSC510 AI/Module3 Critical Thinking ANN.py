""" Simple ANN demo for credit default prediction.
Refreshes basics: forward/backprop, loss, activation.
Dataframe is a small sample for demo purposes. """

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Sample data
data_training = {
    'credit_history': ['bad', 'good'],
    'amount': [1169, 4870],
    'job': ['yes', 'no'],
    'default': ['no', 'yes']
}
df = pd.DataFrame(data_training, index=['applicant1', 'applicant2'])
print(df)

# feature processing
credit_history_encoder = LabelEncoder().fit(df['credit_history'])
job_encoder = LabelEncoder().fit(df['job'])
scaler = StandardScaler().fit(df[['amount']])

def data_processing(df):
    df['credit_history'] = credit_history_encoder.transform(df['credit_history'])
    df['job'] = job_encoder.transform(df['job'])
    df['amount'] = scaler.transform(df[['amount']])
    X = df[['credit_history', 'amount', 'job']].values.astype(np.float32)
    y = (df['default'] == 'yes').astype(np.float32).values.reshape(-1, 1) if 'default' in df.columns else None
    return X, y

X, y = data_processing(df)

# ANN setup
input_size = X.shape[1]
hidden_size = 4
output_size = 1
learning_rate = 0.1

weight1 = np.random.randn(input_size, hidden_size) * 0.01
bias1 = np.zeros(hidden_size)
weight2 = np.random.randn(hidden_size, output_size) * 0.01
bias2 = np.zeros(output_size)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict(X_input, weight1, bias1, weight2, bias2): #forward propagation
    hidden_output = sigmoid(np.dot(X_input, weight1) + bias1)
    output = sigmoid(np.dot(hidden_output, weight2) + bias2)
    return [output,  hidden_output]

# Training/ backpropagation
for epoch in range(1000):
    output,  hidden_output = predict(X, weight1, bias1, weight2, bias2)
    error2 = (output - y)
    # gradient for output layer
    delta2 = error2 * output * (1 - output)
    d_weight2 = np.dot(hidden_output.T, delta2) / len(X)
    d_bias2 = np.mean(delta2, axis=0)
    
    # gradient for hidden layer activation
    error1 = np.dot(delta2, weight2.T)
    delta1 = error1 * hidden_output * (1 - hidden_output)
    
    # gradient for hidden layer weights and biases
    d_weight1 = np.dot(X.T, delta1) / len(X)
    d_bias1 = np.mean(delta1, axis=0)
    
    weight1 -= learning_rate * d_weight1
    bias1 -= learning_rate * d_bias1
    weight2 -= learning_rate * d_weight2
    bias2 -= learning_rate * d_bias2
    
    if epoch % 100 == 0:  
        loss = np.mean(0.5 * (error2**2)) 

train_preds,_ = predict(X, weight1, bias1, weight2, bias2)

print('Credit Default Prediction Demo')
print('_' * 20)
for idx, (pred, actual) in zip(df.index, zip(train_preds.ravel(), y.ravel())):
    print(f"{idx:10}  Probability: {pred:.4f}  Prediction: {int(actual)}")

# User input
credit_history = input("Enter credit history ('bad' or 'good'): ").strip()
amount = float(input("Enter loan amount in whole number (e.g., 1169, 4870): ").strip())
job = input("Enter job status ('yes', 'no'): ").strip()

user_row = pd.DataFrame([{
    'credit_history': credit_history,
    'amount': amount,
    'job': job
}])

X_user, _ = data_processing(user_row)
user_input_predict,_ = predict(X_user, weight1, bias1, weight2, bias2)
user_prediction_prob = user_input_predict[0,0]
user_prediction_text = "low default risk" if user_prediction_prob < 0.5 else "default risk"
print(f"Prediction for the applicant: {user_prediction_text} (Probability: {user_prediction_prob:.4f})")
print('End of the credit default prediction demo. Thank you for using this tool!')
