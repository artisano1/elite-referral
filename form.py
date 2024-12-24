import streamlit as st
    import requests

    def main():
        # Create a form for free opportunity subscription
        with st.form("opportunity_form"):
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            submit_button = st.form_submit_button("Submit")

        # Send the opportunity subscription information to the Telegram bot
        if submit_button:
            opportunity_info = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            }
            response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/sendMessage", json=opportunity_info)
            if response.status_code == 200:
                st.success("Opportunity subscription information sent successfully!")
            else:
                st.error("Error sending opportunity subscription information")

        # Create a social media sharing button
        st.button("Share on Social Media")

    if __name__ == "__main__":
        main()
