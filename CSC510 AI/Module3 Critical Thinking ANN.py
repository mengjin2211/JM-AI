""" Simple ANN demo for credit default prediction.
Refreshes basics: forward/backprop, loss, activation.
Dataframe is a small sample for demo purposes. """

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Sample data
data_training = {
    'credit_history': ['bad', 'good'],
    'amount': [1169, 4870],
    'job': ['yes', 'no'],
    'default': ['no', 'yes']
}
df = pd.DataFrame(data_training, index=['applicant1', 'applicant2'])
print(df)

# Encoders and scaler
credit_history_encoder = LabelEncoder().fit(df['credit_history'])
job_encoder = LabelEncoder().fit(df['job'])
scaler = MinMaxScaler().fit(df[['amount']])

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
 
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size) * 0.01
b1 = np.zeros(hidden_size)
W2 = np.random.randn(hidden_size, output_size) * 0.01
b2 = np.zeros(output_size)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict(X): #forward propagation
    hidden_output = sigmoid(np.dot(X, W1) + b1)
    output = sigmoid(np.dot(hidden_output, W2) + b2)
    return [output,  hidden_output]

# Training/ backpropagation
for epoch in range(1000):
    output,  hidden_output=predict(X)
    d_loss = (output - y)
    # gradient for output layer
    dW2 = np.dot(hidden_output.T, d_loss * output * (1 - output)) / len(X)
    db2 = np.mean(d_loss * output * (1 - output), axis=0)
    # gradient for hidden layer activation
    d_hidden = np.dot(d_loss * output * (1 - output), W2.T) * hidden_output * (1 - hidden_output)
    # gradient for hidden layer weights and biases
    dW1 = np.dot(X.T, d_hidden) / len(X)
    db1 = np.mean(d_hidden, axis=0)
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

train_preds,_ = predict(X)

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
user_input_predict,_ = predict(X_user)
print(f"Probability of default for the applicant: {user_input_predict[0,0]:.4f}")
print('End of the credit default prediction demo. Thank you for using this tool!')
