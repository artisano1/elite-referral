import schedule
    import time
    import requests

    def send_follow_up_message(chat_id, message):
        # Send a follow-up message to the lead
        response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/sendMessage", json={"chat_id": chat_id, "text": message})
        if response.status_code == 200:
            print("Follow-up message sent successfully!")
        else:
            print("Error sending follow-up message")

    def main():
        # Schedule the follow-up messages
        schedule.every(1).to(3).days.do(send_follow_up_message, chat_id=123456789, message="Follow-up message 1")
        schedule.every(1).to(3).days.do(send_follow_up_message, chat_id=123456789, message="Follow-up message 2")
        # Add more follow-up messages as needed

        while True:
            schedule.run_pending()
            time.sleep(1)

    if __name__ == "__main__":
        main()
