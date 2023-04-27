""" 
KNN manual implementation
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

# Load data
iris = load_iris()

# Split data into train and test
X = iris.data
y = iris.target

# Define hyperparameters
k = 3

# Define functions
def euclid_dist(x1, x2):
    """ 
    Euclidean distance between two points
    """
    return np.sqrt(np.sum((x1 - x2)**2))

def get_neighbours(data,k):
    """ 
    Get k nearest neighbours
    """
    euclid_dist(x1, x2)
    pass

def predict_class():
    """ 
    Predict class of test data
    """
    pass