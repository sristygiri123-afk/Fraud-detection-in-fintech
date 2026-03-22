import streamlit as st
import joblib
import pandas as pd
import numpy as np
import datetime
from style import load_css
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random
import time




# ==============================
# LOAD MODEL
# ==============================
@st.cache_resource
def load_model():
    return joblib.load("fraud_detection_model_smote.pkl")
model = load_model()

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:
    st.markdown("### 📊 Dataset Stats")
    st.metric("Total Transactions", "2,84,807")
    st.metric("Fraud Cases", "492")
    st.metric("Model Accuracy", "94%")

# ==============================
# LOAD CSS
# ==============================
load_css()

# ==============================
# LOAD DATA
# ==============================
@st.cache_data
def load_data():
    file_id = "12yY4BxGbe4ysO61I3YsGDMhklb8GazGO"
    url = f"https://drive.usercontent.google.com/download?id={file_id}&export=download&confirm=t"
    return pd.read_csv(url, nrows=10000)

df = load_data()
st.write(df.shape)
st.write(df.columns.tolist())
st.stop()
X = df.drop("Class", axis=1)

# ==============================
# SAVE TRANSACTION FUNCTION
# ==============================
def save_transaction(amount, time, fraud_prob, result):
    new_data = pd.DataFrame([{
        "Amount": amount,
        "Time": time,
        "Fraud_Probability": fraud_prob,
        "Result": result
    }])
    try:
        new_data.to_csv("history.csv", mode='a', header=False, index=False)
    except:
        new_data.to_csv("history.csv", index=False)

# ==============================
# HELPER FUNCTION
# ==============================
def glass_card(title, func):
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    if title:
        st.subheader(title)
    func()
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================
st.markdown("# 💳 Fraud Detection System")
with st.expander("ℹ️ About this Model"):
    st.write("Algorithm: Logistic Regression")
    st.write("Trained on: 284,807 transactions")
    st.write("Balanced using: SMOTE")
    st.write("Features: 30 (Time, V1-V28, Amount)")

# ==============================
# TIME
# ==============================
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
seconds_since_midnight = now.hour * 3600 + now.minute * 60 + now.second

# ==============================
# INPUT SECTION
# ==============================
amount = 0.0
threshold = 50

def input_section():
    global amount, threshold
    amount = st.number_input("Enter Transaction Amount (₹)", min_value=0.0, step=0.01)
    st.write(f"⏱ Time: {now.strftime('%H:%M:%S')}")
    threshold = st.slider("⚙️ Sensitivity (%)", 0, 90, 50)
    if threshold < 40:
        st.warning("⚠️ High sensitivity: May flag legitimate transactions as fraud")
    elif threshold > 70:
        st.info("ℹ️ Low sensitivity: Some frauds might be missed")

glass_card("🧾 Enter Transaction Details", input_section)

# ==============================
# BUTTON — sirf prediction karo aur session me save karo
# ==============================
if st.button("🔍 Check Transaction", key="check_txn"):
    if amount == 0.0:
        st.warning("Please enter a valid transaction amount.")
    else:
        # Nearest neighbor lookup
        differences = abs(X['Amount'] - amount)
        closest_index = differences.idxmin()
        input_data = X.loc[closest_index].copy()

        # Amount normalize + Time override
        input_data['Amount'] = (amount - X['Amount'].mean()) / X['Amount'].std()
        input_data['Time'] = seconds_since_midnight

        # DataFrame
        input_df = pd.DataFrame([input_data])
        input_df = input_df[model.feature_names_in_]

        # Prediction
        probability = model.predict_proba(input_df)

        # Session state me save karo
        st.session_state.fraud_prob = probability[0][1] * 100
        st.session_state.legit_prob = probability[0][0] * 100
        st.session_state.amount_used = amount
        st.session_state.threshold_used = threshold
        st.session_state.show_result = True
        st.session_state.history_saved = False  # ✅ FIX 1: har naye transaction pe reset

        # Naye transaction pe OTP reset karo
        if "generated_otp" in st.session_state:
            del st.session_state.generated_otp

# ==============================
# RESULTS — button ke bahar, session state se
# ==============================
if st.session_state.get("show_result"):
    fraud_prob = st.session_state.fraud_prob
    legit_prob = st.session_state.legit_prob
    amount = st.session_state.amount_used
    threshold = st.session_state.threshold_used

    # ==============================
    # GRAPH
    # ==============================
    st.markdown("### 📊 Fraud Probability Analysis")
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(["Legitimate", "Fraud"], [legit_prob, fraud_prob],
           color=["green", "red"])
    ax.set_ylabel("Probability (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Transaction Risk Distribution")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.pyplot(fig)

    # ==============================
    # SUMMARY CARD
    # ==============================
    def summary():
        c1, c2 = st.columns(2)
        c1.metric("Amount", f"₹{amount:.2f}")
        c2.metric("Time", now.strftime('%H:%M:%S'))
    glass_card("📊 Transaction Summary", summary)

    # ==============================
    # RESULT CARD
    # ==============================
    def result():
        result_label = ""

        if fraud_prob < threshold:
            st.success("🟢 Low Risk - Transaction Approved")
            st.progress(int(legit_prob))
            result_label = "Low Risk"

        elif fraud_prob < (threshold + 20):
            st.warning("🟡 Medium Risk - OTP Verification Required")
            st.progress(int(fraud_prob))

            # OTP generate karo sirf ek baar
            if "generated_otp" not in st.session_state:
                st.session_state.generated_otp = str(random.randint(100000, 999999))

            st.info(f"📱 Demo OTP: **{st.session_state.generated_otp}**")
            otp_input = st.text_input("Enter OTP to approve transaction", key="otp_input")

            if otp_input:
                if otp_input == st.session_state.generated_otp:
                    st.success("✅ OTP Verified - Transaction Approved!")
                    result_label = "Approved after OTP"
                    del st.session_state.generated_otp
                else:
                    st.error("❌ Wrong OTP - Transaction Blocked!")
                    result_label = "Blocked - Wrong OTP"

        else:
            st.error("🔴 High Risk - Transaction BLOCKED")
            st.progress(int(fraud_prob))
            result_label = "High Risk"

        # POSSIBLE REASONS
        st.markdown("### 🔍 Possible Reasons")
        reasons = []
        if amount > 50000:
            reasons.append("💸 Unusually high transaction amount")
        if seconds_since_midnight < 20000:
            reasons.append("🌙 Late night transaction")
        if fraud_prob > 80:
            reasons.append("⚠️ Strong anomaly detected")
        if reasons:
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.write("No strong anomaly detected")

        # ✅ FIX 2: Save history sirf ek baar
        if result_label and not st.session_state.get("history_saved"):
            save_transaction(amount, now.strftime('%H:%M:%S'), fraud_prob, result_label)
            st.session_state.history_saved = True

    glass_card("🧠 Risk Analysis", result)

    # ==============================
    # GAUGE METER
    # ==============================
    st.markdown("### 🎯 Risk Meter")
    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=float(fraud_prob),
        title={'text': "Fraud Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"},
            ],
        }
    ))
    st.plotly_chart(fig2, use_container_width=True)

# ==============================
# TRANSACTION HISTORY
# ==============================
st.markdown("### 📈 Transaction History")
if st.checkbox("Show Last Transactions"):
    try:
        df_history = pd.read_csv("history.csv")
        df_history.columns = ["Amount", "Time", "Fraud_Probability", "Result"]

        filter_option = st.selectbox(
            "Filter Transactions",
            ["All", "Only Fraud", "Only Normal"]
        )
        if filter_option == "Only Fraud":
            df_history = df_history[df_history["Result"] == "High Risk"]
        elif filter_option == "Only Normal":
            df_history = df_history[df_history["Result"] == "Low Risk"]

        df_display = df_history.tail(10).reset_index(drop=True)
        df_display.insert(0, "Select", False)

        edited_df = st.data_editor(
            df_display,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Select": st.column_config.CheckboxColumn(
                    "🗑️ Select",
                    help="Select transactions to delete",
                    default=False
                )
            }
        )

        if st.button("🗑️ Delete Selected", key="delete_btn"):
            selected_rows = edited_df[edited_df["Select"] == True]
            if len(selected_rows) == 0:
                st.warning("Please select at least one transaction to delete.")
            else:
                full_history = pd.read_csv("history.csv")
                full_history.columns = ["Amount", "Time", "Fraud_Probability", "Result"]
                for _, row in selected_rows.iterrows():
                    full_history = full_history[
                        ~((full_history["Amount"] == row["Amount"]) &
                          (full_history["Time"] == row["Time"]))
                    ]
                # ✅ FIX 3: rerun hataya, cache clear kiya
                full_history.to_csv("history.csv", index=False, header=False)
                st.success(f"✅ {len(selected_rows)} transaction(s) deleted!")
                #st.cache_data.clear()
                time.sleep(1)
                st.rerun()

        if len(df_history) > 1:
            st.markdown("#### 📉 Fraud Probability Trend")
            st.line_chart(df_history[["Fraud_Probability"]])

    except:
        st.info("No transactions yet.")
