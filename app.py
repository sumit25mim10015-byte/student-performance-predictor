from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Home route - display the form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route - handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        previous_score = float(request.form['previous_score'])
        assignment_score = float(request.form['assignment_score'])
        sleep_hours = float(request.form['sleep_hours'])
        
        # Validate input ranges
        if not (0 <= attendance <= 100):
            return render_template('index.html', error="Attendance must be between 0 and 100")
        
        if not (0 <= previous_score <= 100):
            return render_template('index.html', error="Previous score must be between 0 and 100")
        
        if not (0 <= assignment_score <= 100):
            return render_template('index.html', error="Assignment score must be between 0 and 100")
        
        if not (0 <= study_hours <= 24):
            return render_template('index.html', error="Study hours must be between 0 and 24")
        
        if not (0 <= sleep_hours <= 24):
            return render_template('index.html', error="Sleep hours must be between 0 and 24")
        
        # Prepare input for prediction
        features = np.array([[study_hours, attendance, previous_score, assignment_score, sleep_hours]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Determine risk level based on prediction
        if prediction == "Good":
            risk_level = "Low Risk"
            risk_class = "low"
        elif prediction == "Average":
            risk_level = "Medium Risk"
            risk_class = "medium"
        else:
            risk_level = "High Risk"
            risk_class = "high"
        
        # Analyze each input (for student analysis section)
        analysis = {
            'study_hours': {
                'value': study_hours,
                'status': 'Good' if study_hours >= 5 else 'Average' if study_hours >= 3 else 'Low',
                'icon': '📚'
            },
            'attendance': {
                'value': attendance,
                'status': 'Good' if attendance >= 75 else 'Average' if attendance >= 60 else 'Low',
                'icon': '📅'
            },
            'previous_score': {
                'value': previous_score,
                'status': 'Good' if previous_score >= 70 else 'Average' if previous_score >= 50 else 'Low',
                'icon': '📝'
            },
            'assignment_score': {
                'value': assignment_score,
                'status': 'Good' if assignment_score >= 70 else 'Average' if assignment_score >= 50 else 'Low',
                'icon': '📋'
            },
            'sleep_hours': {
                'value': sleep_hours,
                'status': 'Good' if sleep_hours >= 6 else 'Average' if sleep_hours >= 5 else 'Low',
                'icon': '😴'
            }
        }
        
        # Generate rule-based suggestions
        suggestions = []
        
        if attendance < 75:
            suggestions.append({
                'type': 'warning',
                'text': 'Your attendance is relatively low. Try to attend classes more regularly.'
            })
        else:
            suggestions.append({
                'type': 'success',
                'text': 'Your attendance is in a good range. Keep maintaining it.'
            })
        
        if study_hours < 3:
            suggestions.append({
                'type': 'warning',
                'text': 'Your study time is low. Try maintaining a consistent daily study schedule of at least 3-4 hours.'
            })
        elif study_hours >= 5:
            suggestions.append({
                'type': 'success',
                'text': 'You maintain good study hours. Continue this disciplined approach.'
            })
        
        if previous_score < 50:
            suggestions.append({
                'type': 'warning',
                'text': 'Your previous score indicates that some subjects may need more attention. Consider seeking help from teachers.'
            })
        elif previous_score >= 75:
            suggestions.append({
                'type': 'success',
                'text': 'Your previous academic performance is strong. Keep up the excellent work.'
            })
        
        if assignment_score < 50:
            suggestions.append({
                'type': 'warning',
                'text': 'Try to complete assignments regularly and review difficult topics. Assignments are crucial for learning.'
            })
        elif assignment_score >= 70:
            suggestions.append({
                'type': 'success',
                'text': 'Your assignment completion rate is excellent. This shows good learning habits.'
            })
        
        if sleep_hours < 6:
            suggestions.append({
                'type': 'warning',
                'text': 'Consider maintaining a healthier sleep schedule. Adequate sleep (6-8 hours) is essential for memory and concentration.'
            })
        elif sleep_hours >= 7:
            suggestions.append({
                'type': 'success',
                'text': 'You maintain a healthy sleep schedule. This supports better learning and retention.'
            })
        
        # Return result with all information
        return render_template('index.html', 
                             prediction=prediction,
                             risk_level=risk_level,
                             risk_class=risk_class,
                             suggestions=suggestions,
                             analysis=analysis,
                             # Pass input values for display
                             input_study_hours=study_hours,
                             input_attendance=attendance,
                             input_previous_score=previous_score,
                             input_assignment_score=assignment_score,
                             input_sleep_hours=sleep_hours)
    
    except ValueError:
        return render_template('index.html', error="Please enter valid numerical values")
    except Exception as e:
        return render_template('index.html', error="An error occurred. Please try again.")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)