# Credit Risk Modelling

This project presents a data science approach to credit risk analysis, aimed at predicting the likelihood of default based on financial data. It combines exploratory data analysis, model experimentation, and interactive deployment to demonstrate how data science can support decision-making in financial and security contexts.

## Overview

Using Python and popular data science libraries, the project begins with data visualization to uncover trends and relationships within the dataset. Tools like `pandas`, `matplotlib`, and `seaborn` were used to explore features such as income, housing status, employment, and credit history.

Several classification algorithms were implemented and compared, including Decision Tree, Random Forest, Extra Trees, and XGBoost. Each model was tuned using `GridSearchCV` to optimize hyperparameters and improve predictive performance. Accuracy scores and other metrics were used to evaluate model effectiveness, with special attention paid to handling class imbalance through techniques like `class_weight` and `scale_pos_weight`.

## Streamlit App

To make the model accessible and interactive, a user interface was built using `Streamlit`. The app allows users to input new data points and receive real-time predictions about credit risk. It also displays model insights such as feature importance and performance metrics, making it both informative and user-friendly.

## Technologies Used

- Python
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- xgboost
- streamlit

## How to Run

1. Clone the repository
2. Launch the app with `streamlit run app.py`

## Purpose

This project serves as a practical demonstration of how machine learning can be applied to financial risk assessment. It’s designed for educational purposes, portfolio building, and as a foundation for more advanced credit scoring systems. 

## Sample Interface
![CREDIT RISK PROJECT](My%20image.png)



