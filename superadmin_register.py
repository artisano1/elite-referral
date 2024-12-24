import streamlit as st
    import requests
    from database import insert_superadmin_info

    def main():
        st.title("Superadmin Registration")
        st.markdown("""
            <style>
                body {
                    background-color: #f4f4f4;
                    font-family: Arial, sans-serif;
                }
                .container {
                    max-width: 400px;
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
        st.markdown('<h1>Superadmin Registration</h1>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="form">', unsafe_allow_html=True)
        with st.form("register_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit_button = st.form_submit_button("Register")

        if submit_button:
            if password == confirm_password:
                superadmin_info = {
                    "username": username,
                    "password": password
                }
                insert_superadmin_info(superadmin_info)
                st.success("Registration successful!")
                # Redirect to superadmin login
                st.experimental_rerun()
            else:
                st.error("Passwords do not match")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()
