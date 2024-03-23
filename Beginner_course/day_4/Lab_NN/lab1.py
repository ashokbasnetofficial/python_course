import numpy as np
class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                # Perceptron update rule
                update = self.lr * (y_[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def _unit_step_func(self, x):
        return np.where(x >= 0, 1, 0)

# Given training dataset
X = np.array([
    [5.9, 75],
    [5.8, 86],
    [5.2, 50],
    [5.4, 55],
    [6.1, 85],
    [5.5, 62]
])

# Classes where 'Male' is 1 and 'Female' is 0
y = np.array([1, 1, 0, 0, 1, 1])


p = Perceptron(learning_rate=0.02, n_iters=1000)
p.fit(X, y)

test_inputs = np.array([[6.0764,77.1136],[5.9400,86.750], [5.9979, 81.2432],[5.4144, 58.0020],[5.4761,54.7691],[5.4444, 50.8754]])
predictions = p.predict(test_inputs)

print(predictions)
