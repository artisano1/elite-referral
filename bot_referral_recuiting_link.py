import streamlit as st
    import requests

    def main():
        # Create a bot referral recruiting link system
        with st.form("referral_form"):
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            submit_button = st.form_submit_button("Submit")

        # Send the referral information to the Telegram bot
        if submit_button:
            referral_info = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            }
            response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/sendMessage", json=referral_info)
            if response.status_code == 200:
                st.success("Referral information sent successfully!")
            else:
                st.error("Error sending referral information")

        # Create a bot referral recruiting link
        st.button("Get Referral Link")

    if __name__ == "__main__":
        main()
