import streamlit as st

    def main():
        st.title("Welcome to Arvea Elite Referral Business")
        st.markdown("""
            <style>
                body {
                    background-color: #f4f4f4;
                    font-family: Arial, sans-serif;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                .header {
                    text-align: center;
                    margin-bottom: 20px;
                }
                .header h1 {
                    color: #333;
                }
                .header p {
                    color: #666;
                }
                .form {
                    display: flex;
                    flex-direction: column;
                }
                .form input {
                    margin-bottom: 10px;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                .form button {
                    padding: 10px;
                    background-color: #007bff;
                    color: #fff;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                .form button:hover {
                    background-color: #0056b3;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="container">', unsafe_allow_html=True)
        st.markdown('<div class="header">', unsafe_allow_html=True)
        st.markdown('<h1>Join Our Referral Program</h1>', unsafe_allow_html=True)
        st.markdown('<p>Sign up to start earning commissions from your referrals.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="form">', unsafe_allow_html=True)
        with st.form("lead_form"):
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            national_id = st.text_input("National ID")
            country = st.text_input("Country")
            phone_number = st.text_input("Phone Number")
            submit_button = st.form_submit_button("Submit")

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
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()
