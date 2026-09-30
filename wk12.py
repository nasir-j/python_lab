import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate 1000 random values
np.random.seed(42)

x1 = np.random.rand(1000)
x2 = np.random.rand(1000)
c = np.random.rand(1000)

# Calculate y
y = x1**2 + 3*x2 + c

# Features
X = np.column_stack((x1, x2))

# Convert features to polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y, test_size=0.2, random_state=42
)

# Train Polynomial Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Check score
score = model.score(X_test, y_test)

print("Model Score:", score)