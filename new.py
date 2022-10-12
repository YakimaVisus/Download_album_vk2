# -*- coding: utf-8 -*-
import os
import sys
import urllib
import urllib.request
import colorama
from colorama import Fore, Style
from colorama import init
import requests
import json
init()
token = ''


def main():
    
    # получаем альбом
    print(Style.RESET_ALL + '''
    Мы имеем:
        https://vk.com/album1488_008
        https://vk.com/albumЭТО_ИЭТО
    Нужно вписать:
        1488_008
    Если с группы:
        -1488_008
    __________________________
    Автор скрипта: Yakima Visus
    ''')

    yakimavisus = input('[]Введите ссылку на альбом: ')

    id_albom = yakimavisus.split('_')[-1]
    id_user = yakimavisus.split('_')[0]
    newpath = os.path.join(sys.path[0], id_user)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    r = requests.get('https://api.vk.com/method/photos.get', params={'owner_id':id_user,'access_token':token,'rev':0,'extended':1,'album_id':id_albom,'count':1000,'photo_sizes': True, 'v':5.131 }) #в случае ошибак обновсите 'v'
    data = (r.json())
    with open('photos.json', 'w+',encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        for i in range(len(data["response"]["items"])):
                photo_url = str(data["response"]["items"][i]["sizes"][4]["url"])
                print(Fore.GREEN + f"[{i}] - фотка загружена " + str(data["response"]["items"][i]['id']))
                urllib.request.urlretrieve(photo_url, newpath + '/' + str(data["response"]["items"][i]['id']) + '.jpg')
    # работаем с каждой полученной фотографией
    print(Fore.LIGHTGREEN_EX + "[]Загрузка началась...")

if __name__ == "__main__":
    main()
