""" CSC510 - Module 3: Critical Thinking
Simple ANN demo for Credit Default Prediction
This demo helps me refresh the basic components 
including forward propagation, backpropagation, loss, and activation functions.
A dataframe is created to resemble my final project. """
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Create a df to resemble my final project dataset
data = {
    'credit_history': ['critical', 'good'],
    'amount': [1169, 4870],
    'job': ['skilled', 'skilled'],
    'dependents': [1, 2],
    'default': ['no', 'yes']  # This is the label 
}

# Create the DataFrame correctly
df = pd.DataFrame(data, index=['applicant1', 'applicant2'])
print(df)

def prepare_data(df, include_label=True):
    cat_cols = ['credit_history', 'job']
    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))
    num_cols = ['amount', 'dependents']
    scaler = MinMaxScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    X = df[cat_cols + num_cols].values.astype(np.float32)
    y = None
    if include_label and 'default' in df.columns:
        y = (df['default'] == 'yes').astype(np.float32).values.reshape(-1, 1)

    return X, y


# ANN
def ANN(X):
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

    for epoch in range(epochs):
        hidden_output = sigmoid(np.dot(X, W1) + b1)
        output = sigmoid(np.dot(hidden_output, W2) + b2)
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

    hidden_output = sigmoid(np.dot(X, W1) + b1)
    prediction = sigmoid(np.dot(hidden_output, W2) + b2)
    return prediction


def train_ANN(X, y):
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

    for epoch in range(epochs):
        hidden_output = sigmoid(np.dot(X, W1) + b1)
        output = sigmoid(np.dot(hidden_output, W2) + b2)
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

    return W1, b1, W2, b2

def predict_ANN(X, W1, b1, W2, b2):
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    hidden_output = sigmoid(np.dot(X, W1) + b1)
    prediction = sigmoid(np.dot(hidden_output, W2) + b2)
    return prediction

def safe_input(prompt, cast_func, valid_values=None):
    while True:
        value = input(prompt).strip()
        try:
            if valid_values and value not in valid_values:
                print(f"Please enter one of the following: {valid_values}")
                continue
            return cast_func(value)
        except Exception:
            print(f"Invalid input. Please enter a valid value.")

def main ():

    X_train, y_train = prepare_data(df, include_label=True)
    W1, b1, W2, b2 = train_ANN(X_train, y_train)

    print('Credit Default Prediction Demo')
    print('_' * 20)
    train_preds = predict_ANN(X_train, W1, b1, W2, b2)
    for idx, (pred, actual) in zip(df.index, zip(train_preds.ravel(), y_train.ravel())):
        print(f"{idx:10}  Probability: {pred:.4f}  Prediction: {int(actual)}")

    # User Input Section
    print("Please enter the details for the applicant:")


    user_data = {
        'credit_history': safe_input(
            "Enter credit history (e.g., 'critical', 'good'): ",
            str,
            valid_values=['critical', 'good']
        ),
        'amount': safe_input(
            "Enter loan amount (e.g., 1169, 4870): ",
            float
        ),
        'job': safe_input(
            "Enter job type (e.g., 'skilled', 'unskilled'): ",
            str,
            valid_values=['skilled', 'unskilled']
        ),
        'dependents': safe_input(
            "Enter number of dependents (whole number, e.g., 1, 2, 3): ",
            int
        )
    }

    df_user = pd.DataFrame([user_data], index=['user_input'])
    X_user, _ = prepare_data(df_user, include_label=False)
    user_pred = predict_ANN(X_user, W1, b1, W2, b2)

    print(f"Probability of default for the applicant: {user_pred[0][0]:.4f}")
    print('End of the credit default prediction demo. Thank you for using this tool!')
if __name__ == "__main__":
    main()
