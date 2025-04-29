import telebot

bot = telebot.TeleBot('7410629472:AAG8XXOKdSYYiwlU9q-IbH7tQmYGG3VUE8E')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, f"Приветствую тебя {message.from_user.first_name}!")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id, "Я создан чтобы ты исправил свою жизнь!")



@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Здравствуйте!")

    # разработчик это я
    elif message.text.lower() == "разработчик":
        bot.send_message(message.from_user.id, "https://www.instagram.com/v_v_moon?igsh=MTk0ams3ajV5Y3czNA%3D%3D&utm_source=qr")


    # 3 кодовых слова:
    elif message.text.lower() == "википедия":
        bot.send_message(message.from_user.id, "https://ru.wikipedia.org/wiki/Заглавная_страница")

    elif message.text.lower() == "ютуб":
        bot.send_message(message.from_user.id, "https://www.youtube.com")

    elif message.text.lower() == "что-то еще":
        bot.send_message(message.from_user.id, "https://www.kinopoisk.ru/series/5048763/?utm_referrer=www.google.com")
    # конец кодовых слов

    else:
        bot.send_message(message.from_user.id, "Бот на стадии разработки:/")

bot.polling(none_stop=True) #позволяет боту работать 24/7