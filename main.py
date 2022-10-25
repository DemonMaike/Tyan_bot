from msilib.schema import Directory
from requests import delete
import telebot

import os

ID_ADMIN = '718580248'
ID_GROUP = '-1001542389568'


bot = telebot.TeleBot('5722083415:AAHrlDH2hVRgS601pe7AX1ap5t8PYdhUr7w')

def main():
    photo_url = []
    # перебераем фото, сохраняем лист
    directory = 'photo'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        photo_url.append(f)   
    # Отправляем первый эллемент списка в группу, удаляем, информируем сколько фото осталось, если не получется, то пишем, что фото закончились
    try:
        photo = open(photo_url[0], 'rb')  
        bot.send_photo(ID_GROUP, photo)
        photo.close()
        os.remove(photo_url[0])
        bot.send_message(ID_ADMIN, f'{len(photo_url)} фото осталось')
    except:
        bot.send_message(ID_ADMIN, 'Фото закончились')
        
if __name__ == "__main__":
    main()