""" CSC510 - Module 3: Critical Thinking
Simple ANN demo for Credit Default Prediction"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Create a df to resemble my final project dataset
data = {
    'checking_balance': ['< 0 DM', '1 - 200 DM'],
    'months_loan_duration': [6, 24],
    'credit_history': ['critical', 'good'],
    'purpose': ['furniture/appliances', 'car'],
    'amount': [1169, 4870],
    'savings_balance': ['unknown', '< 100 DM'],
    'employment_duration': ['> 7 years', '1 - 4 years'],
    'percent_of_income': [4, 3],
    'years_at_residence': [4, 4],
    'age': [67, 53],
    'job': ['skilled', 'skilled'],
    'dependents': [1, 2],
    'default': ['no', 'yes']
}
df = pd.DataFrame(data, index=['applicant1', 'applicant2'])
print (df) 
cat_cols = ['checking_balance', 'credit_history', 'purpose', 'savings_balance', 'employment_duration', 'job']

# Prepare the cat and num columns
for col in cat_cols:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

num_cols = ['months_loan_duration', 'amount', 'percent_of_income', 'years_at_residence', 'age', 'dependents']
scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

X = df[cat_cols + num_cols].values.astype(np.float32)
y = (df['default'] == 'yes').astype(np.float32).values.reshape(-1, 1)

# ANN
input_size = X.shape[1]
hidden_size = 4
output_size = 1
learning_rate = 0.1
epochs = 1000

np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size) * 0.01
b1 = np.zeros(hidden_size)
W2 = np.random.randn(hidden_size, output_size) * 0.01
b2 = np.zeros(output_size)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)

for epoch in range(epochs):
    hidden_output = sigmoid(np.dot(X, W1) + b1)
    output = sigmoid(np.dot(hidden_output, W2) + b2)
    loss = np.mean((output - y) ** 2)
    d_loss = (output - y)
    dW2 = np.dot(hidden_output.T, d_loss * output * (1 - output)) / len(X)
    db2 = np.mean(d_loss * output * (1 - output), axis=0)
    d_hidden = np.dot(d_loss * output * (1 - output), W2.T) * hidden_output * (1 - hidden_output)
    dW1 = np.dot(X.T, d_hidden) / len(X)
    db1 = np.mean(d_hidden, axis=0)
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss:.4f}')


hidden_output = sigmoid(np.dot(X, W1) + b1)

# Prediction
prediction = sigmoid(np.dot(hidden_output, W2) + b2)
print('Credit Default Prediction Demo')
print('_'*20)
for idx, (pred, actual) in zip(df.index, zip(prediction.ravel(), y.ravel())):
    print(f"{idx:10}  Probability: {pred:.4f}  Prediction: {int(actual)}")


"""I learned about ANN a few years. This demo helps me refresh the basic components 
including forwardpropagation, backpropagation, loss and activation functions.
A dataframe is created to resemble my final project. """