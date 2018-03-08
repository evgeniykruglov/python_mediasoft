import requests
import datetime
#import transliterate
from time import sleep
from transliterate import translit, get_available_language_codes


url = "https://api.telegram.org/bot520075736:AAHoRHoWW5KDIzTJ4mnMspzWEDCYu5UYN5s/"


def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    #print(response.json())
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def get_message(update):
    chat_text = update['message']['text']
    return chat_text

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def transliterator (original_text):
	translit_text = translit(original_text, 'ru')
	return translit_text

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), transliterator(get_message(last_update(get_updates_json(url)))))
           update_id += 1
        sleep(10)       

if __name__ == '__main__':  
    main()
    



