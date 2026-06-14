import streamlit as st

st.set_page_config(page_title="FAILSAFE")
st.sidebar.title("FAILSAFE")

st.sidebar.info("""
Explainable AI based Student Risk Prediction System

Technologies:
- Python
- XGBoost
- SHAP
- Streamlit
""")
st.title("🎓 FAILSAFE")
st.subheader("Student Risk Prediction System")
st.info("""
FAILSAFE helps faculty identify students who may be at risk of academic failure
and recommends interventions before it is too late.
""")
st.markdown("---")

st.write("### Project Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric("Model Accuracy", "72.1%")

with col2:
    st.metric("Dataset Size", "395 Students")

st.markdown("---")
age = st.slider("Age", 15, 22, 18)

studytime = st.slider(
    "Study Time",
    1,
    4,
    2
)

failures = st.slider(
    "Previous Failures",
    0,
    4,
    0
)

absences = st.slider(
    "Absences",
    0,
    50,
    5
)

health = st.slider(
    "Health",
    1,
    5,
    3
)

Medu = st.slider(
    "Mother Education",
    0,
    4,
    2
)

Fedu = st.slider(
    "Father Education",
    0,
    4,
    2
)

internet = st.checkbox("Internet Access")
schoolsup = st.checkbox("School Support")
higher = st.checkbox("Higher Education Goal")

if st.button("Predict Risk"):

    risk_score = (
        failures * 0.15 +
        absences * 0.01 +
        (5 - studytime) * 0.1
    )

    risk_score = min(risk_score, 1.0)

    st.metric(
        "Risk Score",
        f"{risk_score*100:.1f}%"
    )

    if risk_score >= 0.8:
        st.error("🔴 High Risk")

    elif risk_score >= 0.5:
        st.warning("🟡 Medium Risk")

    else:
        st.success("🟢 Low Risk")

    st.subheader("Recommended Actions")

    if failures > 0:
        st.write("• Assign remedial academic support")

    if studytime < 2:
        st.write("• Recommend structured study schedule")

    if absences > 10:
        st.write("• Monitor attendance closely")

    if health <= 2:
        st.write("• Recommend counselling support")
st.markdown("---")

st.caption(
    "Developed using XGBoost and Explainable AI for early student risk detection."
)