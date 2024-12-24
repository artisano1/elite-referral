import streamlit as st
    import requests

    def main():
        # Create a compensation plan modification
        st.title("Compensation Plan Modification")

        # Create a form for updating the compensation plan
        with st.form("update_compensation_plan_form"):
            plan_name = st.text_input("Plan Name")
            plan_details = st.text_area("Plan Details")
            submit_button = st.form_submit_button("Update Compensation Plan")

        # Update the compensation plan
        if submit_button:
            plan_info = {
                "plan_name": plan_name,
                "plan_details": plan_details
            }
            response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/updateCompensationPlan", json=plan_info)
            if response.status_code == 200:
                st.success("Compensation plan updated successfully!")
            else:
                st.error("Error updating compensation plan")

    if __name__ == "__main__":
        main()
