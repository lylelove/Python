import numpy as np
from sklearn import datasets, linear_model

diabetes_X_train = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
diabetes_X_test = np.array([[10],[12],[13],[14]])

# Split the targets into training/testing sets
diabetes_y_train = np.array([[2651],[2543],[2494],[2087],[1765],[1538],[1484],[1290],[1226],[1204]])

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)
