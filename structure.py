import numpy as np

# Step 1: random data for now
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) 
y = np.array([0, 0, 0, 1])  

# Step 2: initialize weights and bias
weights = np.random.rand(2)  # random weights for 2 features, 1-e4
bias = 0  

# Step 3: hyperparameters
learning_rate = 0.1
epochs = 1000

# Step 4: training
for epoch in range(epochs):
    for i in range(len(X)):
        
        # Step 5: calculate the weighted sum
        weighted_sum = np.dot(X[i], weights) + bias
        
        # Step 6: activation function
        prediction = 1 if weighted_sum >= 0 else 0
        
        # Step 7: compute the error
        error = y[i] - prediction
        
        # Step 8 & 9: update weights and bias
        weights += learning_rate * error * X[i]
        bias += learning_rate * error

# Step 10: Evaluate performance (using the same training set)
for i in range(len(X)):
    weighted_sum = np.dot(X[i], weights) + bias
    prediction = 1 if weighted_sum >= 0 else 0
    print(f"Input: {X[i]}, Prediction: {prediction}, Actual: {y[i]}")
