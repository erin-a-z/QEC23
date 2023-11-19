import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
time = np.random.rand(100) * 10
xco2 = np.polyval([1, -2, 5, 0, 3], time) + np.random.randn(100) * 10  # Replace with your own coefficients

def get_pred(time, xco2, tf, degree=8):
    # Perform nth order polynomial regression
    coefficients = np.polyfit(time, xco2, degree)
    polynomial = np.poly1d(coefficients)

    # Create a range of x values for the regression line
    x_range = np.linspace(time[-1], tf, 100)

    # Calculate corresponding y values using the polynomial
    y_pred = polynomial(x_range)

    return [x_range, y_pred]

