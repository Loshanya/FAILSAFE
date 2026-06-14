# FAILSAFE
Explainable AI based Student Failure Prediction System
# 🎓 FAILSAFE

## Explainable AI-Based Student Risk Prediction System

FAILSAFE is an intelligent student risk prediction system designed to identify students who may be at risk of academic failure before final semester results are declared. The system uses Machine Learning and Explainable AI techniques to provide early warnings and actionable intervention recommendations for faculty members.

---

## Problem Statement

In educational institutions, student failure is often detected only after final examination results, leaving little opportunity for meaningful intervention.

FAILSAFE addresses this challenge by:

- Identifying at-risk students early.
- Predicting failure risk using academic and behavioral factors.
- Providing transparent explanations for predictions.
- Recommending interventions to improve student outcomes.

---

## Objectives

- Predict students at risk of academic failure.
- Enable early intervention by faculty.
- Provide explainable predictions using SHAP.
- Generate personalized recommendations for at-risk students.
- Support data-driven academic decision making.

---

## Dataset

**UCI Student Performance Dataset**

Dataset Features Include:

- Age
- Study Time
- Previous Failures
- Absences
- Health Status
- Family Background
- Parental Education
- School Support
- Internet Access
- Career Aspirations
- Academic Performance Indicators

Dataset Size:

- 395 Student Records
- 33 Original Features

---

## Technology Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- SHAP

### Dashboard

- Streamlit

### Visualization

- Matplotlib

---

## Project Workflow

```text
Student Data
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
XGBoost Classification Model
      ↓
Risk Prediction
      ↓
SHAP Explainability
      ↓
Intervention Recommendations
```

---

## Models Developed

### Model 1: Mid-Semester Prediction

Uses previous academic scores (G1 and G2).

**Accuracy: 87%**

Advantages:

- Higher predictive accuracy
- Better identification of at-risk students

---

### Model 2: Early Warning System

Excludes G1 and G2 to allow earlier intervention.

**Accuracy: 72.1%**

Advantages:

- Can identify risk before major examinations
- Supports proactive faculty intervention

---

## Key Features

- Student Failure Risk Prediction
- Explainable AI using SHAP
- Risk Probability Scoring
- High / Medium / Low Risk Classification
- Automated Intervention Recommendations
- Interactive Streamlit Dashboard

---

## Sample Output

### Risk Assessment

```text
Risk Score: 87%

Risk Level: High Risk
```

### Recommended Actions

```text
• Assign remedial academic support
• Recommend structured study schedule
• Monitor attendance closely
• Provide counselling support
```

---

## Explainable AI

The project uses **SHAP (SHapley Additive exPlanations)** to explain model predictions.

Benefits:

- Transparency
- Interpretability
- Faculty-friendly insights
- Trustworthy predictions

---

## Dashboard

The Streamlit dashboard allows faculty members to:

- Enter student information
- Predict academic risk
- View risk levels
- Receive intervention recommendations

---

## Future Scope

- React.js Frontend
- FastAPI Backend
- PostgreSQL Database
- Faculty Login System
- Student Monitoring Dashboard
- Real-Time Analytics
- Automated Email Alerts
- Intervention Tracking System

---

## Results

| Model | Description | Accuracy |
|---------|-------------|----------|
| Model 1 | With G1 & G2 | 87% |
| Model 2 | Early Warning Model | 72.1% |

---

## Team Project

FAILSAFE demonstrates the application of Machine Learning and Explainable AI for improving academic outcomes through proactive student support and intervention.
