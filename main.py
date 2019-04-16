import json
import websocket

import pygame
import pyperclip
import requests

import settings


poe_filter = None


def on_message_2(ws, message):
    print(message)
    print(poe_filter)


def on_message(ws, message):
    new_ids = json.loads(message)
    new_ids = new_ids["new"]
    new_id = new_ids[len(new_ids) - 1]

    req_url = settings.SEARCH_URL.format(new_id, poe_filter)
    r = requests.get(req_url)

    result_json = json.loads(r.text)
    result_json = result_json["result"]

    if result_json:
        final_result = result_json[0]["listing"]["whisper"]

        pyperclip.copy(final_result)
        
        pygame.mixer.init()
        pygame.mixer.music.load("beep.wav")
        pygame.mixer.music.play()


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


if __name__ == "__main__":   
    f = open('dump.txt', 'r')
    loaded_dict = json.loads(f.read())
    f.close()

    poesessid = input("Please enter your POESESSID [{}]: ".format(loaded_dict['poesessid'])) or loaded_dict['poesessid']
    poe_filter = input("Please enter your filter [{}] : ".format(loaded_dict['poe_filter'])) or loaded_dict['poe_filter']

    my_dict = {"poesessid": poesessid, "poe_filter": poe_filter}
    f = open('dump.txt', 'w+')
    f.write(json.dumps(my_dict))
    f.close()

    session = requests.Session()
    response = session.get('https://www.pathofexile.com')

    my_cookie = '__cfuid={}; POESESSID={}'.format(session.cookies.get_dict()['__cfduid'], poesessid)

    ws = websocket.WebSocketApp('ws://www.pathofexile.com/api/trade/live/{}/{}'.format(settings.LEAGUE, poe_filter),
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close,
                                cookie = my_cookie)
    ws.run_forever()