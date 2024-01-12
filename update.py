import numpy as np

def update_parameters(weights, biases, x, y, lr="proportional"):
    m = len(y)  # Number of training examples
    predictions = np.dot(x, weights) + biases
    errors = predictions - y

    if lr == "proportional":
        learning_rate = 1.0 / np.sqrt(1 + np.arange(1, m))
    else:
        learning_rate = lr

    weights -= (1/m) * learning_rate * np.dot(x.T, errors)
    biases -= (1/m) * learning_rate * np.sum(errors)

    return weights, biases

# Example usage:
# Replace 'your_data' and 'your_targets' with your actual data and target values
x = np.array([[1, 2], [2, 3], [3, 4]])
y = np.array([3, 5, 7])
weights = np.zeros(x.shape[1])
biases = 0.0

# Update parameters using gradient descent
updated_weights, updated_biases = update_parameters(weights, biases, x, y)

print("Updated Weights:", updated_weights)
print("Updated Biases:", updated_biases)
