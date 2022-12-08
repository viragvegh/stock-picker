import constants
import requests


def send_message(message):
    url = f"https://api.telegram.org/bot{constants.api_key}/sendMessage?chat_id={constants.chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message
