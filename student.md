# Project Statement

## Project Title

Student Performance Predictor

## Problem Statement

Students may face academic difficulties due to factors such as insufficient study time, low attendance, previous academic performance, assignment performance, and poor sleep habits. However, it can be difficult to identify students who may require academic support at an early stage.

The proposed system uses Machine Learning to analyze selected student-related parameters and classify the student's performance into one of three categories:

- Good
- Average
- At Risk

The system also provides rule-based suggestions based on the student's input values.

## Scope of the Project

The project focuses on predicting student performance using a Machine Learning classification model.

The system accepts the following inputs:

- Study Hours
- Attendance Percentage
- Previous Exam Score
- Assignment Score
- Sleep Hours

Based on these inputs, the trained Decision Tree Classifier predicts the student's performance category.

The project is intended as an educational demonstration of Machine Learning classification and does not guarantee a student's actual future academic performance.

## Target Users

The target users of the system are:

1. Students who want to understand their current performance category.
2. Teachers or mentors who want a simple indication of possible academic risk.
3. Academic project evaluators who want to demonstrate the application of Machine Learning in education.

## High-Level Features

### 1. Student Input and Validation

The user enters academic and lifestyle-related information through a web form.

The system validates the entered values before making a prediction.

### 2. Machine Learning Prediction

The system uses a trained Decision Tree Classifier to classify the student into:

- Good
- Average
- At Risk

### 3. Result and Risk Analysis

The predicted performance category is displayed to the user along with a corresponding risk level:

- Good → Low Risk
- Average → Medium Risk
- At Risk → High Risk

### 4. Personalized Suggestions

The system provides rule-based suggestions based on the student's input values.

Examples include suggestions related to:

- Study hours
- Attendance
- Previous academic score
- Assignment performance
- Sleep duration

## Technology Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML5
- CSS3

## Machine Learning Model

The project uses a Decision Tree Classifier for multiclass classification.

The model is trained using student academic and behavioral features and predicts one of three performance categories.

## Expected Input

The system accepts:

- Study Hours
- Attendance Percentage
- Previous Exam Score
- Assignment Score
- Sleep Hours

## Expected Output

The system produces:

- Predicted Performance Category
- Risk Level
- Student Metric Analysis
- Rule-Based Improvement Suggestions
