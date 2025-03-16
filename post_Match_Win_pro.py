import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset (Assuming we have past match stats)
data = pd.read_csv("pre_match_data.csv")

# Selecting relevant features
features = ["team1_strength", "team2_strength", "venue_win_pct", 
            "batting_first_win_pct", "last_5_match_form_t1", "last_5_match_form_t2",
            "head_to_head_t1", "head_to_head_t2", "top_batsman_avg", "top_bowler_economy"]

X = data[features]
y = data["winner"]  # 1 for Team 1 win, 0 for Team 2 win

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Example: Predict probability for an upcoming match
new_match = pd.DataFrame([[80, 75, 60, 55, 4, 3, 7, 5, 45, 6.5]], columns=features)
new_match = scaler.transform(new_match)
win_prob = model.predict_proba(new_match)[:, 1][0]
print(f"Win Probability for Team 1: {win_prob * 100:.2f}%")

