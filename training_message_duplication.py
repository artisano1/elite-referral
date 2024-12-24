import schedule
    import time
    import requests

    def send_training_message(chat_id, message):
        # Send a training message to the lead
        response = requests.post("https://api.telegram.org/bot8142180415:AAGwVJZ1wnO-Ma7v6OzfS7TGxpQomLwpAro/sendMessage", json={"chat_id": chat_id, "text": message})
        if response.status_code == 200:
            print("Training message sent successfully!")
        else:
            print("Error sending training message")

    def main():
        # Schedule the training messages
        schedule.every(1).to(2).days.do(send_training_message, chat_id=123456789, message="Training message 1")
        schedule.every(1).to(2).days.do(send_training_message, chat_id=123456789, message="Training message 2")
        # Add more training messages as needed

        while True:
            schedule.run_pending()
            time.sleep(1)

    if __name__ == "__main__":
        main()
