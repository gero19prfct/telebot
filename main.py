import telebot

TOKEN = '6934660504:AAG0YVy2sFNgkQKBrRYkH7bsYuU8JZLK82U'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,"Напишите ИИН")

@bot.message_handler(content_types=['text'])
def talk(message):
    if(message.text.isnumeric() and len(message.text)==12):
        bot.send_message(message.chat.id,"Успешно сделано")
    if(message.text.isnumeric() and (len(message.text)>12 or len(message.text)<12)) :
        bot.send_message(message.chat.id,"не правилно")
    if(message.text.isnumeric()==False):
        bot.send_message(message.chat.id,"Напишите ИИН")    
    


bot.polling(none_stop=True)