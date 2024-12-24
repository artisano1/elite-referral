import streamlit as st
    import requests

    def main():
        # Create a backoffice for admin
        st.title("Backoffice for Admin")

        # Create a form for updating message templates
        with st.form("update_template_form"):
            template_name = st.text_input("Template Name")
            template_message = st.text_area("Template Message")
            submit_button = st.form_submit_button("Update Template")

        # Update the message template
        if submit_button:
            template_info = {
                "template_name": template_name,
                "template_message": template_message
            }
            response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/updateTemplate", json=template_info)
            if response.status_code == 200:
                st.success("Template updated successfully!")
            else:
                st.error("Error updating template")

        # Create a form for sending update notifications
        with st.form("send_notification_form"):
            notification_message = st.text_area("Notification Message")
            submit_button = st.form_submit_button("Send Notification")

        # Send the update notification
        if submit_button:
            notification_info = {
                "notification_message": notification_message
            }
            response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/sendNotification", json=notification_info)
            if response.status_code == 200:
                st.success("Notification sent successfully!")
            else:
                st.error("Error sending notification")

    if __name__ == "__main__":
        main()
