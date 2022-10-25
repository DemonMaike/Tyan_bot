import telebot

bot = telebot.TeleBot('5722083415:AAHrlDH2hVRgS601pe7AX1ap5t8PYdhUr7w')

@bot.message_handler(content_types=['text'])

def chatid(message):
    print(message.chat.id)
    

bot.polling()