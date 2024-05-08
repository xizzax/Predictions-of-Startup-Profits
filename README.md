# Profit Prediction Project

This project aims to predict the profit of startups based on various factors such as R&D spending, administration costs, marketing spending, and the location (state) of the startup. It utilizes machine learning regression models to make accurate profit predictions.

## Dataset
The dataset used in this project contains information about 50 startups, including their R&D spending, administration costs, marketing spending, state (location), and profit.

## Exploratory Data Analysis (EDA)
The project begins with exploratory data analysis to understand the distribution of the data, identify any outliers, and explore the relationships between different variables such as R&D spending, administration costs, marketing spending, and profit.

## Data Preprocessing
Before training the machine learning models, the dataset undergoes preprocessing steps such as handling categorical data (converting state to numerical values) and splitting the data into training and testing sets.

## Regression Models
Several regression models are trained and evaluated using the dataset to predict startup profits:
- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- SVM Regression
- Ridge Regression
- Lasso Regression


## UI Output
The UI output component of the project provides a user-friendly interface for users to input startup details (R&D spending, administration costs, marketing spending, and state) and get predictions for the startup's profit using the trained Random Forest Regression model. The interface allows users to interactively input data and receive predicted profit values.

## Project Structure
The project directory includes the following components:
- `notebook.ipynb`: Jupyter Notebook containing the code for data exploration, preprocessing, model training, and evaluation.
- `ui.py`: Python script for the UI output component, which utilizes the trained Random Forest Regression model to make predictions based on user input.
- `startups_50.csv`: Dataset containing information about 50 startups.
- `model_RF.joblib`: Serialized Random Forest Regression model trained on the dataset.
- `stock.png`: Image used for UI background.
- `README.md`: Documentation providing an overview of the project, its components, and usage instructions.

## Usage
To use the UI output component:
1. Ensure that Python and the required libraries (including tkinter and joblib) are installed.
2. Run the `ui.py` script.
3. Input the R&D spending, administration costs, marketing spending, and state (location) of the startup.
4. Click the "Predict" button to receive the predicted profit value.

![image](https://github.com/xizzax/Predictions-of-Startup-Profits/assets/76040683/14dcfbb0-4237-4ea1-af46-d7a243fca0fd)


## Contributors
- ![Izza Naeem](https://github.com/xizzax)
- ![Ahmad Mahmood](https://github.com/ahmaddioxide/ahmaddioxide) 

## License
This project is licensed under the [MIT License](LICENSE).
