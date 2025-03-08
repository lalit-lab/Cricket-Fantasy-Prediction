# Cricket Fantasy Prediction Model

## 📌 Overview
This project is a **Cricket Fantasy Prediction Model** that helps users predict player performance based on various statistical factors. The model assigns a **performance score** to each player, helping fantasy cricket users make informed decisions when selecting their team.

## 🚀 Features
- **Player Performance Analysis**: Uses multiple factors to evaluate a player's potential performance.
- **Fantasy Points Prediction**: Calculates a player's impact based on past fantasy scores.
- **Weighted Scoring System**: Balances different statistical aspects to give an overall score.
- **User-Friendly Interface**: Built using **Streamlit** for easy interaction.

## 🔢 How It Works
The model calculates a player's **Overall Score** using the following factors:

| Factor                        | Weight (%)  | Description  |
|-------------------------------|------------|-------------|
| **Form Index**                | 20%        | Performance in last 5 matches |
| **Venue Impact**              | 20%        | Performance at the given venue vs overall career |
| **H2H Performance**           | 15%        | Performance against the specific opponent |
| **1st Innings Average**       | 7.5%       | Batting average in the 1st innings |
| **2nd Innings Average**       | 7.5%       | Batting average in the 2nd innings |
| **Fantasy Points Per Match**   | 25%        | Average fantasy points per match |
| **Pressure Performance Score**| 5%         | Player's performance in high-pressure situations |

### 📊 Score Interpretation
- **Score > 25** → 🔥 **Excellent Pick** (Must-have player)
- **Score 15 - 25** → ✅ **Good Pick** (Safe choice)
- **Score 5 - 15** → ⚠️ **Risky Pick** (Depends on other factors)
- **Score < 5** → ❌ **Avoid** (Poor recent form or unfavorable conditions)

## 🛠 Installation & Usage
### **1. Clone the Repository**
```bash
git clone https://github.com/lalit-lab/Cricket-Fantasy-Prediction.git
cd Cricket-Fantasy-Prediction
```

### **2. Install Dependencies**
Make sure you have **Python 3.x** installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
```bash
streamlit run app.py
```
This will open a local Streamlit web app where you can enter player data and get predictions.

## 📂 Project Structure
```
Cricket-Fantasy-Prediction/
│── app.py                # Streamlit application
│── data/                 # Sample datasets (if any)
│── models/               # Any saved models (if used)
│── requirements.txt      # Python dependencies
│── README.md             # Project Documentation
```

## 🤝 Contribution
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License
This project is open-source and available under the **MIT License**.
