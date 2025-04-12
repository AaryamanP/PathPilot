import streamlit as st

st.set_page_config(page_title="Login | PathPilot", page_icon="🔐")

st.title("🔐 Sign Up / Log In")

option = st.radio("Choose an option:", ["Sign Up", "Log In"], horizontal=True)

if option == "Sign Up":
    st.subheader("📝 Create a New Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    if st.button("Create Account"):
        if password == confirm and email:
            st.success("Account created successfully! (Placeholder logic)")
        else:
            st.error("Passwords do not match or email missing.")
else:
    st.subheader("🔑 Log In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        # Placeholder logic
        st.success("Logged in! (Placeholder logic)")
