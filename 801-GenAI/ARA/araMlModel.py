# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:20:42 2024

@author: AMITAVA

A python module for functions to predict a numerical score based on a set of features
Features: arrivalDate, lengthOfStay, reservationSCore, upgrateType
the function utilizes an ensemble technique for regression,
evaluates the final model and 
prints performance metrics after prediction 

Please note the following:
    This example assumes that the dataset is in a CSV file with columns including 'arrivalDate', 'lengthOfStay', 'reservationScore', 'upgradeType', and the target variable 'score'.
    The RandomForestRegressor is used as the ensemble model. You can explore other ensemble techniques as needed.
    The performance metrics (Mean Squared Error, Mean Absolute Error, R-squared) are printed after making predictions on the test set.
    You should uncomment and modify the example usage section based on your specific dataset and use case.

Remember to replace "your_dataset.csv" with the actual file path or URL of your dataset in the example usage section.
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV

def prepare_data(data):
    # Assume 'cost' is the target column in your data
    target_column = 'cost'

    # Extract features and target variable
    data = data.drop(columns=['arrivalDateTime'])
    X = data.drop(columns=[target_column])
    y = data[target_column]

    return X,y

def tune_and_evaluate(data):
    """
    Tunes hyperparameters, trains a RandomForestRegressor, and evaluates performance.

    Parameters:
    - data (pd.DataFrame): DataFrame with features (arrivalDate, lengthOfStay, reservationScore, upgradeType) and target variable.

    Returns:
    - RandomForestRegressor: Trained RandomForestRegressor model.
    """
    X, y = prepare_data(data)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define a hyperparameter grid to search
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Create a RandomForestRegressor
    model = RandomForestRegressor(random_state=42)

    # Use GridSearchCV to find the best hyperparameters
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    # Print the best hyperparameters
    print("Best Hyperparameters:", grid_search.best_params_)

    # Train the model with the best hyperparameters
    best_model = grid_search.best_estimator_

    # Make predictions on the test set
    predictions = best_model.predict(X_test)

    # Evaluate the model on the testing set
    calculate_metrics(y_test, predictions)

    return best_model


def predict_score(data, model):
    """
    Predicts a numerical score based on a set of features using RandomForestRegressor.

    Parameters:
    - data (pd.DataFrame): DataFrame with features (arrivalDate, lengthOfStay, reservationScore, upgradeType).

    Returns:
    - float: Predicted numerical score.
    """

    X, y = prepare_data(data)
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if (model==None):
        # Create and train the RandomForestRegressor
        model = RandomForestRegressor() #(n_estimators=100, random_state=42)

    print('Using Model: ',model)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    est = make_pipeline(StandardScaler(), model)
    est.fit(X_train, y_train)
    
    #model.fit(X_train, y_train)

    # Make predictions on the test set
    #predictions = model.predict(X_test)
    predictions = est.predict(X_test)

    # Evaluate the model
    calculate_metrics(y_test, predictions)

    # Return the predicted score for demonstration purposes
    return X_test, predictions




def calculate_metrics(y_test, predictions):

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # Print performance metrics
    #Mean Squared Error (MSE): MSE measures the average squared difference between actual and predicted values.
    #Lower MSE values are better, indicating smaller errors on average.
    #However, the interpretation of "small" or "large" depends on the scale of our target variable.
    #print(f"Mean Squared Error (ideally should be 0): {mse:.4f}")
    
    #Mean Absolute Error (MAE): MAE measures the average absolute difference between actual and predicted values.
    #Lower MAE values are better, and like MSE, the interpretation depends on the scale of the target variable.
    #print(f"Mean Absolute Error (closer to 0): {mae:.4f}")

    #R-squared (R2): R-squared measures the proportion of the variance in the dependent variable that is 
    #predictable from the independent variables.
    #Higher R-squared values (closer to 1) are generally better. 
    #A value of 1 indicates that the model explains all the variability in the target variable.    
    print(f"R-squared (closer to 1): {r2:.4f}")


# Example usage:
# if __name__ == "__main__":
#     # Load your dataset into a DataFrame
#     data = pd.read_csv("your_dataset.csv")

#     # Call the predict_score function
#     predicted_score = predict_score(data)

#     print(f"Predicted Score: {predicted_score:.2f}")