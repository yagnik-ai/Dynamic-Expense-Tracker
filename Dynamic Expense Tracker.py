import streamlit as st

if "categories" not in st.session_state:
    st.session_state.categories = {"Food": 0.0, "Travel": 0.0, "Fun": 0.0, "Other": 0.0}
if "daily_total" not in st.session_state:
    st.session_state.daily_total = 0.0

def add_expense(category, amount):
    if category in st.session_state.categories:
        st.session_state.categories[category] += amount
    else:
        st.session_state.categories["Other"] += amount
    st.session_state.daily_total += amount

def show_summary():
    total = st.session_state.daily_total
    if total == 0:
        st.info("No expenses recorded yet.")
        return
    st.subheader("Expense Summary")
    for category, amount in st.session_state.categories.items():
        percentage = (amount / total) * 100
        st.write(f"- {category}: ₹{amount:.2f} ({percentage:.2f}%)")
    st.write(f"*Total Spent*: ₹{total:.2f}")

st.title("Simple Expense Tracker")

st.sidebar.header("Add Expense")
category = st.sidebar.selectbox("Choose a category", options=list(st.session_state.categories.keys()))
amount = st.sidebar.number_input("Amount", min_value=0.0, step=0.01)

if st.sidebar.button("Add"):
    if amount > 0:
        add_expense(category, amount)
        st.sidebar.success(f"Added ₹{amount:.2f} to {category}")
    else:
        st.sidebar.warning("Please enter a valid amount.")

if st.button("Show Summary"):
    show_summary()

st.write("---")
st.caption("Made by a beginner.")