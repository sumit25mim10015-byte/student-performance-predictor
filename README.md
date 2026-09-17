# 🎓 Student Performance Predictor

A Machine Learning web application that predicts student academic performance based on study habits, attendance, and academic scores using Decision Tree Classifier.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Dataset Information](#dataset-information)
- [Machine Learning Algorithm](#machine-learning-algorithm)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [How to Run](#how-to-run)
- [Usage Instructions](#usage-instructions)
- [Functional Modules](#functional-modules)
- [Model Evaluation](#model-evaluation)
- [Screenshots](#screenshots)
- [Example Prediction](#example-prediction)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)

---

## 🎯 Project Overview

The **Student Performance Predictor** is a beginner-level Machine Learning project developed for the **Introduction to AI & ML** course. The system analyzes student academic and behavioral data to predict their performance category and provides personalized suggestions for improvement.

The application uses a **Decision Tree Classifier** to categorize students into three performance levels:
- ✅ **Good** - Student is performing well
- ⚠️ **Average** - Student needs improvement
- 🚨 **At Risk** - Student requires immediate attention

---

## 🔍 Problem Statement

Many students struggle academically without understanding the underlying factors affecting their performance. Early identification of at-risk students can help educators and parents intervene timely with appropriate support and guidance.

**Challenge:** How can we predict student performance based on their study habits and academic history?

**Solution:** Build a Machine Learning classification model that analyzes student data and predicts performance categories while providing actionable suggestions.

---

## 🎯 Objectives

1. **Predict** student academic performance using Machine Learning
2. **Identify** at-risk students early for timely intervention
3. **Analyze** individual academic metrics (study hours, attendance, scores, sleep)
4. **Provide** personalized, rule-based suggestions for improvement
5. **Demonstrate** practical application of Machine Learning in education
6. **Create** a user-friendly web interface for easy interaction

---

## ✨ Features

### Core Features
- 📊 **Performance Prediction** - Classifies students into Good/Average/At Risk
- 🎯 **Risk Level Assessment** - Assigns Low/Medium/High risk levels
- 📈 **Individual Metric Analysis** - Evaluates each input parameter separately
- 💡 **Personalized Suggestions** - Provides rule-based recommendations
- ✅ **Input Validation** - Ensures data integrity with range checking
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile devices

### User Interface Features
- Clean and professional design
- Step-by-step process visualization
- Interactive input forms with helpful hints
- Color-coded result indicators
- Detailed analysis cards
- Model information display

---

## 🛠️ Technology Stack

### Backend
- **Python 3.x** - Programming language
- **Flask** - Web framework for building the application
- **Scikit-learn** - Machine Learning library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Joblib** - Model serialization

### Frontend
- **HTML5** - Structure and content
- **CSS3** - Styling and layout
- **Jinja2** - Templating engine (integrated with Flask)

### Development Tools
- Visual Studio Code (recommended)
- Git (version control)
- Python pip (package manager)

---

## 📊 Dataset Information

### Dataset Specifications
- **File:** `student_performance.csv`
- **Total Records:** 200 student samples
- **Features:** 5 input variables
- **Target Variable:** 1 categorical output (performance)

### Features Description

| Feature | Description | Range | Type |
|---------|-------------|-------|------|
| **study_hours** | Daily study hours | 0-24 | Continuous |
| **attendance** | Class attendance percentage | 0-100 | Continuous |
| **previous_score** | Last exam score | 0-100 | Continuous |
| **assignment_score** | Assignment completion score | 0-100 | Continuous |
| **sleep_hours** | Daily sleep hours | 0-24 | Continuous |
| **performance** | Performance category (Target) | Good/Average/At Risk | Categorical |

### Dataset Distribution
- **Good Performance:** ~40% of students
- **Average Performance:** ~35% of students
- **At Risk:** ~25% of students

### Sample Data
```csv
study_hours,attendance,previous_score,assignment_score,sleep_hours,performance
8,95,92,94,8,Good
5,78,75,77,6,Average
2,58,55,57,5,At Risk
