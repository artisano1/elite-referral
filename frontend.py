import streamlit as st
    import requests

    def main():
        # Create a frontend for active distributors
        st.title("Frontend for Active Distributors")

        # Create a form for managing downline
        with st.form("manage_downline_form"):
            downline_name = st.text_input("Downline Name")
            downline_email = st.text_input("Downline Email")
            submit_button = st.form_submit_button("Manage Downline")

        # Manage the downline
        if submit_button:
            downline_info = {
                "downline_name": downline_name,
                "downline_email": downline_email
            }
            response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/manageDownline", json=downline_info)
            if response.status_code == 200:
                st.success("Downline managed successfully!")
            else:
                st.error("Error managing downline")

    if __name__ == "__main__":
        main()
