import streamlit as st
    import requests

    # Set up the Streamlit app
    st.title("Arvea Elite Referral Business")

    # Create a form for lead information
    with st.form("lead_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        national_id = st.text_input("National ID")
        country = st.text_input("Country")
        phone_number = st.text_input("Phone Number")
        submit_button = st.form_submit_button("Submit")

    # Send the lead information to the Telegram bot
    if submit_button:
        lead_info = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "national_id": national_id,
            "country": country,
            "phone_number": phone_number
        }
        response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/sendMessage", json=lead_info)
        if response.status_code == 200:
            st.success("Lead information sent successfully!")
        else:
            st.error("Error sending lead information")
