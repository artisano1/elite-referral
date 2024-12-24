import streamlit as st
    import requests

    def main():
        # Create a multilevel structure
        st.title("Multilevel Structure")

        # Create a form for adding new distributors
        with st.form("add_distributor_form"):
            distributor_name = st.text_input("Distributor Name")
            distributor_email = st.text_input("Distributor Email")
            submit_button = st.form_submit_button("Add Distributor")

        # Add the new distributor
        if submit_button:
            distributor_info = {
                "distributor_name": distributor_name,
                "distributor_email": distributor_email
            }
            response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/addDistributor", json=distributor_info)
            if response.status_code == 200:
                st.success("Distributor added successfully!")
            else:
                st.error("Error adding distributor")

    if __name__ == "__main__":
        main()
