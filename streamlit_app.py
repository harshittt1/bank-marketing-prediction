import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(page_title="Bank Marketing Predictor", layout="wide")

# Load model
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    st.error("❌ Failed to load model. Check file path.")
    st.stop()

# Title
st.title("🏦 Bank Marketing Prediction System")
st.write("Predict whether a customer will subscribe to a term deposit.")

# Layout
col1, col2 = st.columns(2)

# LEFT COLUMN
with col1:
    st.subheader("👤 Customer Info")

    age = int(st.number_input("Age", 18, 100, step=1))
    job = st.selectbox("Job", ["admin.", "technician", "services", "management",
                               "retired", "blue-collar", "student", "unemployed",
                               "self-employed", "entrepreneur", "housemaid"])

    marital = st.selectbox("Marital Status", ["married", "single", "divorced"])
    education = st.selectbox("Education", ["primary", "secondary", "tertiary"])
    default = st.selectbox("Credit Default", ["yes", "no"])

    balance = int(st.number_input("Account Balance", step=1))
    housing = st.selectbox("Housing Loan", ["yes", "no"])
    loan = st.selectbox("Personal Loan", ["yes", "no"])

# RIGHT COLUMN
with col2:
    st.subheader("📞 Campaign Details")

    contact = st.selectbox("Contact Type", ["cellular", "telephone", "unknown"])
    day = st.slider("Last Contact Day", 1, 31)
    month = st.selectbox("Month", ["jan","feb","mar","apr","may","jun",
                                  "jul","aug","sep","oct","nov","dec"])

    duration = int(st.number_input("Call Duration (seconds)", step=1))
    campaign = int(st.number_input("Campaign Contacts", step=1))

    pdays = int(st.number_input("Days Since Last Contact (-1 = never)", step=1))
    previous = int(st.number_input("Previous Contacts", step=1))
    poutcome = st.selectbox("Previous Outcome", ["unknown", "failure", "success"])

# Divider
st.markdown("---")

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame([{
        'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'default': default,
        'balance': balance,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'day': day,
        'month': month,
        'duration': duration,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # Probability display
    st.write(f"📊 Probability: {probability*100:.1f}%")
    st.progress(int(probability * 100))

    # Prediction result
    if prediction == 1:
        st.success("✅ Customer WILL subscribe")
    else:
        st.error("❌ Customer will NOT subscribe")

    # Interpretation
    if probability > 0.75:
        st.success("High chance")
    elif probability > 0.5:
        st.info("Moderate chance")
    else:
        st.warning("⚠️ Low chance")

reasons = []

# Duration impact
if duration > 600:
    reasons.append("Long call duration increases likelihood of subscription")
elif duration < 200:
    reasons.append("Short call duration reduces likelihood of subscription")

# Previous outcome
if poutcome == "success":
    reasons.append("Previous campaign success strongly increases probability")
elif poutcome == "failure":
    reasons.append("Previous campaign failure reduces probability")

# Previous contacts
if previous > 0:
    reasons.append("Customer has been contacted before, indicating engagement")

# Balance
if balance > 3000:
    reasons.append("Higher account balance suggests better financial capacity")

# Display reasons
if reasons:
    st.markdown("Key Factors Influencing Prediction")
    for r in reasons:
        st.write(f"• {r}")

if not reasons:
    reasons.append("No strong factors detected; prediction based on overall weak signals")