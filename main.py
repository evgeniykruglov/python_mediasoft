import requests
import datetime
import sys
from time import sleep
from transliterate import translit, get_available_language_codes

def get_updates_json(request):  
    params = {'timeout': 100, 'offset': request}
    response = requests.get(request + 'getUpdates', data=params, timeout=100)
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    try:
        chat_id = update['message']['chat']['id']
    except KeyError:
        chat_id = update['edited_message']['chat']['id']
    return chat_id

def get_edited_chat_id(update):  
    chat_id = update['edited_message']['chat']['id']
    return chat_id

def get_message(update):
    chat_text = update['message']['text']
    return chat_text

def get_edited_message(update):
    chat_text = update['edited_message']['text']
    return chat_text

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def transliterator (original_text, param):
    translit_text = translit(original_text, 'ru', reversed=param)
    return translit_text

def rus_and_eng_converter (param):
    if param == True:
        result = 'RUS to ENG'
    elif param == False:
        result = 'ENG to RUS'
    return result

def first_char_parser (string):
    first_char = string[0]
    #for i in string:
    return first_char

def get_config_message (param, lang):
    lang = rus_and_eng_converter (param)
    result = 'Текущая конфигурация: ' + lang
    return result


def main():
    update_id = last_update(get_updates_json(url))['update_id']
    reverse = False
    language = rus_and_eng_converter (reverse)
    #message = 'Текушая конфигурация: ' + language
    hello_message = """Вас приветствует телеграм бот "Транслитератор v.0.1"!\nВведите любой текст на латинице и я переведу его в кириллицу \nКоманды для бота
    /help - вывести информацию о приложении
    /to-eng - переключить транслитерацию на RUS to ENG
    /to-rus - переключить транслитерацию на ENG to RUS\n"""
    error_message = 'Неверная команда\nВведите /help для получения справки'
    while True:
        try:
            last_response = last_update(get_updates_json(url)) 
            #print (get_updates_json(url))
            if last_response == None:
                print ('!')
            if update_id == last_response['update_id']:                
                try: 
                    if get_message(last_response) == '/help' or get_message(last_response) == '/start': 
                        send_mess(get_chat_id(last_response), hello_message + get_config_message(reverse,language))
                    elif get_message(last_response) == '/to-eng':
                        reverse = True                                           
                        send_mess(get_chat_id(last_response), get_config_message(reverse,language))
                    elif get_message(last_response) == '/to-rus':
                        reverse = False
                        send_mess(get_chat_id(last_response), get_config_message(reverse,language))
                    elif first_char_parser(get_message(last_response)) == '/':
                        send_mess(get_chat_id(last_response), error_message)
                    else:
                        send_mess(get_chat_id(last_response), transliterator(get_message(last_response), reverse))
                except KeyError:
                        send_mess(get_edited_chat_id(last_response), transliterator(get_edited_message(last_response), reverse))
                update_id += 1
            sleep(5) 
        except ReadTimeout:
            continue

if __name__ == '__main__':
    token = sys.argv[1]
    print ("Bot has been started \nToken = " + token)
    url = "https://api.telegram.org/bot" + token + "/"
    main()
