from requests import delete
import telebot
from PIL import Image
import os
from urllib.request import urlopen

import yadisk
from secret import TG_TOKEN,ID_ADMIN,ID_GROUP,YA_TOKEN

#Аунтификация
token = YA_TOKEN
ya = yadisk.YaDisk(token=token)
bot = telebot.TeleBot(TG_TOKEN)

def main():
    try:
        # Директория к папке с фото на Диске
        dir_path = '/Телеграм Каналы/Тяночки в крови/фото тянок ТГ'
        # получаем список фоток
        photo = list(ya.listdir(dir_path))
        # берем первое фото
        url_first_photo = photo[0]['file']
        # Открываем фотку
        img = Image.open(urlopen(url_first_photo))
        #Отправляем в группу
        bot.send_photo(ID_GROUP, photo=img)
        #Удаляем использованую фотку
        ya.remove(photo[0]['path'])
        #Отправляем остаток фото
        bot.send_message(ID_ADMIN, f'{len(photo)} фото осталось')
    except:
        bot.send_message(ID_ADMIN, 'Фото закончились')
    
    
        
if __name__ == "__main__":
    main()