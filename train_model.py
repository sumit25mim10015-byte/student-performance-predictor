# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
print("Loading dataset...")
data = pd.read_csv('student_performance.csv')

# Display first few rows
print("\nDataset Preview:")
print(data.head())

# Separate features (X) and target (y)
X = data[['study_hours', 'attendance', 'previous_score', 'assignment_score', 'sleep_hours']]
y = data['performance']

# Split dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Create Decision Tree Classifier
print("\nTraining the model...")
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Display classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'model.pkl')
print("\nModel saved as 'model.pkl'")
print("Training completed successfully!")