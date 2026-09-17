# 🎓 Student Performance Predictor

A Machine Learning web application that predicts student academic performance based on study habits, attendance, previous academic scores, assignment performance, and sleep hours using a Decision Tree Classifier.

The application provides a predicted performance category, corresponding risk level, individual metric analysis, and rule-based suggestions for improvement.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Scope](#-scope)
- [Target Users](#-target-users)
- [Functional Modules](#-functional-modules)
- [Features](#-features)
- [Non-Functional Requirements](#-non-functional-requirements)
- [Technology Stack](#-technology-stack)
- [System Workflow](#-system-workflow)
- [Dataset Information](#-dataset-information)
- [Machine Learning Model](#-machine-learning-model)
- [Model Selection Rationale](#-model-selection-rationale)
- [Model Training](#-model-training)
- [Model Evaluation](#-model-evaluation)
- [Project Structure](#-project-structure)
- [Installation Guide](#-installation-guide)
- [How to Run](#-how-to-run)
- [Usage Instructions](#-usage-instructions)
- [Example Prediction](#-example-prediction)
- [Testing](#-testing)
- [Screenshots](#-screenshots)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Challenges Faced](#-challenges-faced)
- [Learning Outcomes](#-learning-outcomes)
- [GitHub and Version Control](#-github-and-version-control)
- [References](#-references)
- [License](#-license)

---

## 🎯 Project Overview

The **Student Performance Predictor** is a beginner-level Machine Learning project developed for the **Introduction to AI & ML** course.

The system analyzes selected academic and lifestyle-related student information and uses a trained Machine Learning classification model to predict one of three performance categories:

- ✅ **Good**
- ⚠️ **Average**
- 🚨 **At Risk**

After generating the prediction, the application assigns a corresponding risk level and provides rule-based suggestions based on the student's input values.

The project demonstrates how Machine Learning classification can be integrated into a simple web application using Python and Flask.

> **Important:** The prediction is intended for educational demonstration and does not guarantee a student's actual future academic performance.

---

## 🔍 Problem Statement

Students may experience academic difficulties due to factors such as insufficient study time, low attendance, previous academic performance, assignment performance, and inadequate sleep.

Early identification of students who may require additional academic support can help encourage timely improvement.

### Problem

How can student-related academic and lifestyle information be used to classify a student's current performance category using Machine Learning?

### Proposed Solution

The project develops a web-based Machine Learning system that accepts selected student parameters and uses a **Decision Tree Classifier** to classify the student into:

- Good
- Average
- At Risk

The system also provides a corresponding risk level and rule-based improvement suggestions.

---

## 🎯 Objectives

The main objectives of the project are:

1. Predict student performance using Machine Learning.
2. Classify students into Good, Average, and At Risk categories.
3. Analyze important student-related input parameters.
4. Provide a simple risk-level interpretation of the prediction.
5. Provide rule-based suggestions for possible improvement.
6. Demonstrate the practical application of Machine Learning in education.
7. Develop a simple and user-friendly web interface.
8. Demonstrate integration between a Machine Learning model and a web application.

---

## 📌 Scope

The project focuses on Machine Learning-based classification of student performance using structured numerical data.

The system accepts five input parameters:

- Study Hours
- Attendance Percentage
- Previous Exam Score
- Assignment Score
- Sleep Hours

The trained Decision Tree Classifier processes these inputs and predicts the student's performance category.

The system is designed as an educational project and is not intended to replace professional academic assessment or institutional decision-making.

---

## 👥 Target Users

The intended users of the system are:

### 1. Students

Students can enter their academic and lifestyle information to view their predicted performance category and suggestions.

### 2. Teachers and Mentors

Teachers or mentors can use the system as a simple demonstration tool for identifying students who may require additional academic attention.

### 3. Academic Evaluators

The project demonstrates the practical implementation of Machine Learning classification concepts in an educational application.

---

# ⚙️ Functional Modules

The project contains three major functional modules.

## Module 1 — Student Input and Validation

The user enters:

- Study Hours
- Attendance
- Previous Exam Score
- Assignment Score
- Sleep Hours

The application validates the input values before processing them.

### Input

Student academic and lifestyle information.

### Output

Validated input data or an appropriate validation message.

---

## Module 2 — Machine Learning Prediction

The validated input is passed to the trained **Decision Tree Classifier**.

### Input

Five numerical student features.

### Processing

```text
Student Input
      ↓
Input Validation
      ↓
Decision Tree Classifier
      ↓
Performance Classification
