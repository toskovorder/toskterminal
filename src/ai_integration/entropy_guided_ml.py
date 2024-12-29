from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class EntropyGuidedML:
    def __init__(self, entropy_factor):
        self.entropy_factor = entropy_factor
        self.model = RandomForestClassifier()

    def add_entropy_to_data(self, X):
        noise = np.random.normal(0, self.entropy_factor, size=X.shape)
        return X + noise

    def train(self, X, y):
        X_noisy = self.add_entropy_to_data(X)
        self.model.fit(X_noisy, y)

    def predict(self, X):
        return self.model.predict(X)
