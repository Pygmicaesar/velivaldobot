import requests
import json
import time
import datetime
import urllib

with open("data.json", "r") as read_file:
    data = json.load(read_file)

TOKEN = "773330747:AAEEbN_K8J6CDzeEINANG4UBdsHGlkL0qDg"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
TEXT = "Päivän pakollinen kääpiöviesti"
TEXTOE = "Oeoeoee"

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_chat_id(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (chat_id)

def send_message(chat, text):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat)
    get_url(url)

def main():

    chat = get_last_chat_id(get_updates())

    while True:

        try:
            print("getting updates")
            now = datetime.datetime.now()

            if now.hour == 0  and (now.minute == 0 or now.minute == 1):
                send_message(chat, TEXT)
                time.sleep(2)
                send_message(chat, TEXTOE)
                time.sleep(120)
        
            time.sleep(100)

        except Exception as e:
            print(e)

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        exit()
