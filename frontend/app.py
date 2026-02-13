import sys
import os
sys.path.append(os.path.abspath("../backend"))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from payroll import calculate_salary
from expense_ai import categorize_expense
from prediction import predict_cash_flow
from anomaly import detect_anomaly
from health_score import health_score
from pdf_generator import generate_payslip

st.set_page_config(page_title="FinPilot AI", layout="wide")

st.title("🚀 FinPilot AI - Smart CFO Dashboard")

# ================= PAYROLL =================

st.header("💼 Payroll Management")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Employee Name")
    base = st.number_input("Base Salary", 0)
    overtime = st.number_input("Overtime Hours", 0)
    bonus = st.number_input("Bonus", 0)
    deductions = st.number_input("Deductions", 0)

if st.button("Calculate Payroll"):
    gross, tax, net = calculate_salary(base, overtime, bonus, deductions)

    st.success(f"Net Salary: ₹ {net}")

    file = generate_payslip(name, base, overtime, bonus, deductions, gross, tax, net)

    with open(file, "rb") as f:
        st.download_button(
            label="📥 Download Payslip",
            data=f,
            file_name=file,
            mime="application/pdf"
        )

# ================= EXPENSE =================

st.header("💳 AI Expense Categorization")

desc = st.text_input("Expense Description")
amount = st.number_input("Expense Amount", 0)

if st.button("Categorize Expense"):
    category = categorize_expense(desc)
    st.info(f"Predicted Category: {category}")

# ================= CASH FLOW =================

st.header("📈 Cash Flow Prediction")

expense_data = st.text_area(
    "Enter Monthly Expenses (comma separated)",
    "10000,15000,18000,20000,22000"
)

if st.button("Predict Cash Flow"):
    values = [int(x.strip()) for x in expense_data.split(",")]
    data = [(i + 1, values[i]) for i in range(len(values))]
    predictions = predict_cash_flow(data)

    st.write("Next 3 Month Prediction:", predictions)

    fig = plt.figure()
    plt.plot(values)
    plt.title("Expense Trend")
    st.pyplot(fig)

# ================= ANOMALY =================

st.header("🚨 Anomaly Detection")

if st.button("Detect Anomalies"):
    values = [int(x.strip()) for x in expense_data.split(",")]
    anomalies = detect_anomaly(values)
    st.warning(f"Unusual Expenses Detected: {anomalies}")

# ================= HEALTH SCORE =================

st.header("🏥 Financial Health Score")

col3, col4, col5 = st.columns(3)

with col3:
    revenue = st.number_input("Monthly Revenue", 0)

with col4:
    expenses = st.number_input("Monthly Expenses", 0)

with col5:
    reserve = st.number_input("Cash Reserve", 0)

if st.button("Calculate Health Score"):
    score = health_score(revenue, expenses, reserve)

    st.metric("Health Score", f"{score}/100")

    if score > 75:
        st.success("Startup Financial Health: Strong 💚")
    elif score > 50:
        st.info("Startup Financial Health: Moderate ⚠")
    else:
        st.error("Startup Financial Health: Risky 🔴")
