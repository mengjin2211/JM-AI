""" Simple ANN demo for credit default prediction.
Refreshes basics: forward/backprop, loss, activation.
Dataframe is a small sample for demo purposes. """

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# I started with a small sample data which generated poor predictions. Model struggled to learn.
# Sample data
# data_training = {
#     'credit_history': ['bad', 'good'],
#     'amount': [2069, 4800],
#     'job': ['yes', 'no'],
#     'default': ['no', 'yes']
# }
# Increase training set which is more realistic/consistent and allows the model to learn better.
data_training = {
    'credit': ['bad',  'good', 'bad',  'good', 'bad',  'good', 'good', 'bad'],
    'amount':         [2508, 1006,   4501, 1565,   3090, 850,    410, 6200],
    'job':            ['no',   'yes',  'no',   'yes',  'yes',  'yes',  'no', 'no'],
    'default':        ['yes',  'no',   'yes',  'no',   'yes',  'no',   'no', 'yes']
}
# Dynamically create the index to match the length of the data
df = pd.DataFrame(data_training, index=[f'applicant{i+1}' for i in range(len(data_training['credit']))])
print("Updated Training Data:")
print(df)

# feature processing
credit_history_encoder = LabelEncoder().fit(df['credit'])
job_encoder = LabelEncoder().fit(df['job'])
stdscaler = StandardScaler().fit(df[['amount']])

def data_processing(df):
    df['credit'] = credit_history_encoder.transform(df['credit'])
    df['job'] = job_encoder.transform(df['job'])
    df['amount'] = stdscaler .transform(df[['amount']])
    X = df[['credit', 'amount', 'job']].values.astype(np.float32)
    y = (df['default'] == 'yes').astype(np.float32).values.reshape(-1, 1) if 'default' in df.columns else None
    return X, y

X, y = data_processing(df)

# variables
def initialize_parameters(input_dim, hidden_nodes, output_nodes):
    """Initializes weights and biases for the neural network using Xavier initialization."""
    # Xavier initialization (Glorot initialization) suitable for sigmoid activations
    w1 = np.random.randn(input_dim, hidden_nodes) * np.sqrt(1. / input_dim)
    b1 = np.zeros(hidden_nodes)
    w2 = np.random.randn(hidden_nodes, output_nodes) * np.sqrt(1. / hidden_nodes)
    b2 = np.zeros(output_nodes)
    return w1, b1, w2, b2

# Initialize network parameters
input_size, hidden_size, output_size, learning_rate = X.shape[1], 5, 1, 0.9

weight1, bias1, weight2, bias2 = initialize_parameters(
    input_size, 
    hidden_size, 
    output_size
)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward_propagation (X_input, weight1, bias1, weight2, bias2): 
    hidden_output = sigmoid(np.dot(X_input, weight1) + bias1)
    output = sigmoid(np.dot(hidden_output, weight2) + bias2)
    return [output,  hidden_output]

def ANN_train(X, y, weight1, bias1, weight2, bias2, learning_rate, epochs=1000):
    for epoch in range(epochs):
        output, hidden_output = forward_propagation(X, weight1, bias1, weight2, bias2)
        
        prediction_error = output - y 
        
        delta_at_output = prediction_error * output * (1 - output)
        gradient_weights_out = np.dot(hidden_output.T, delta_at_output) / X.shape[0]
        gradient_bias_out = np.mean(delta_at_output, axis=0)
        
        error_at_hidden = np.dot(delta_at_output, weight2.T)
        delta_at_hidden = error_at_hidden * hidden_output * (1 - hidden_output)
        
        gradient_weights_hidden = np.dot(X.T, delta_at_hidden) / X.shape[0]
        gradient_bias_hidden = np.mean(delta_at_hidden, axis=0)
        
        update_w1 = learning_rate * gradient_weights_hidden
        update_b1 = learning_rate * gradient_bias_hidden
        update_w2 = learning_rate * gradient_weights_out
        update_b2 = learning_rate * gradient_bias_out
        
        weight1 = weight1 - update_w1
        bias1 = bias1 - update_b1
        weight2 = weight2 - update_w2
        bias2 = bias2 - update_b2        

    return weight1, bias1, weight2, bias2
# I will get the weights and biases after training; inside the training, called forward_propagation 

w_input_hidden, b_hidden, w_hidden_output, b_output = ANN_train(X, y, weight1, bias1, weight2, bias2, learning_rate)
#perform a forward pass to get predictions
final_train_predictions, _ = forward_propagation(X, w_input_hidden, b_hidden, w_hidden_output, b_output)

print('Credit Default Prediction Demo')
 
# User input
try:
    credit_history = input("Enter credit history ('bad' or 'good'): ").strip()
    amount = float(input("Enter loan amount in whole number (e.g., 1000, 4800): ").strip())
    job = input("Enter job status ('yes', 'no'): ").strip()

    user_row = pd.DataFrame([{
        'credit': credit_history,
        'amount': amount,
        'job': job
    }])
    X_user, _ = data_processing(user_row)
    # Use forward_propagation and the trained weights/biases
    user_input_predict,_ = forward_propagation(X_user, w_input_hidden, b_hidden, w_hidden_output, b_output)
    user_prediction_prob = user_input_predict[0,0]
    user_prediction_text = "low default risk" if user_prediction_prob < 0.5 else "default risk"
    print(f"Prediction for the applicant: {user_prediction_text} (Probability: {user_prediction_prob:.4f})")

except ValueError as e:
    print(f"Invalid input: {e}.")
except Exception as e:
    print(f"An error occurred: {e}. ")
finally:
    print('Thank you for using this tool!')

"""Instruction to run the script:
VSCode
1)	Navigate to the Script's Directory
2)	Open a terminal and enter  “pip install numpy pandas scikit-learn” to import libraries
3)	Open the CSC510 Week3 –Critical Thinking Ann_new in VScode
4)	Run the script python credit_model.py
5)	Enter user input according to the instruction
6)	Model will predict credit card default probability based on your entry. View prediction. 
If you are using Anaconda Prompt/or Command Prompt, following steps below: 
1.	cd "c:\download folder\"
2.	pip install numpy pandas scikit-learn
3.	python "Module3 Critical Thinking ANN_new.py"
4.	Enter User Input following the instruction
5.	View prediction
"""
