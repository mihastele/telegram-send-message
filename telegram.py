# send-message-to-telegram.py
# by www.ShellHacks.com
import os
import requests

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Get API token from environment variable
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_to_telegram(message):

    apiToken = TELEGRAM_TOKEN
    chatID = CHAT_ID
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Hello from Python!")