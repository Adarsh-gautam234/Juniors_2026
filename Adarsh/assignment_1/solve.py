# solve.py
# Students must complete the TODO sections

import numpy as np

# ============================================================
# OLS IMPLEMENTATIONS
# ============================================================

def ols_with_intercept(X, y):
    """
    Ordinary Least Squares WITH intercept.

    Parameters
    ----------
    X : numpy array (N,d)
        Feature matrix

    y : numpy array (N,)
        Target values

    Returns
    -------
    w  : slope vector (d,)
    w0 : intercept scalar
    """

    # TODO:
    # Step 1: Add a column of ones to X to represent intercept
    # Step 2: Use the normal equation
    #
    #        w = (X^T X)^(-1) X^T y
    #
    # Step 3: Separate intercept from weight vector

    raise NotImplementedError


def ols_no_intercept(X, y):
    """
    OLS WITHOUT intercept.

    Use the normal equation:

        w = (X^T X)^(-1) X^T y
    """

    # TODO:
    # Implement closed-form solution

    raise NotImplementedError


# ============================================================
# PREDICTION FUNCTIONS
# ============================================================

def predict_with_intercept(X, w, w0):
    """
    Predict y = Xw + w0
    """

    # TODO:
    # return predicted values

    raise NotImplementedError


def predict_no_intercept(X, w):
    """
    Predict y = Xw
    """

    # TODO

    raise NotImplementedError


# ============================================================
# METRICS
# ============================================================

def compute_metrics(y, y_hat):
    """
    Compute the following metrics:

    1. Mean Squared Error (MSE)

        MSE = mean((y - y_hat)^2)

    2. Correlation

    3. Squared Correlation

    4. R^2 score
    """

    # TODO

    raise NotImplementedError


# ============================================================
# DATA LOADING
# ============================================================

def load_data():
    """
    Load dataset from CSV files.

    CSV format:

    size,bedrooms,age,distance,price

    First 4 columns = features
    Last column = target
    """

    train = np.loadtxt("train.csv", delimiter=",", skiprows=1)
    test = np.loadtxt("test.csv", delimiter=",", skiprows=1)

    # TODO:
    # Separate X and y

    raise NotImplementedError