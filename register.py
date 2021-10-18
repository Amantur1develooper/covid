import telebot
import  requests
from telebot.types import Message
token = '2097104496:AAFnULf0e3V9i3r339RAoq7sCoPEQuXLhwQ'
p=[]
bot = telebot.TeleBot(token)
@bot.message_handler(commands="start")
def start(message):
    a='Здравствуйте для регистрации нужно вести свои данные: фио,номер.Через запятую)'
    bot.send_message(message.chat.id,a)
    
@bot.message_handler(content_types='text')
def name(message):
    a1=message.text
    t="Данные были приняты)"
    t2="Данные небыли приняты)"
    if ',' in a1:
        for i in a1.split(","):
            p.append(i)
            print(p)
        bot.send_message(message.chat.id,t)
    else:
        bot.send_message(message.chat.id,t2) 
print("Bot is working!")
bot.infinity_polling()