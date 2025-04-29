import telebot, buttons

bot = telebot.TeleBot('7410629472:AAG8XXOKdSYYiwlU9q-IbH7tQmYGG3VUE8E')


print("Бот запущен!")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, f"Приветствую тебя {message.from_user.first_name}!", reply_markup=buttons.choice_button())

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id, "Я бот и у меня есть кнопки")


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == "википедия":
        bot.send_message(message.from_user.id, "Введите слово для поиска")
        bot.register_next_step_handler(message, wiki)

    elif message.text.lower() == "ютуб":
        bot.send_message(message.from_user.id, "Введите слово")
        bot.register_next_step_handler(message, youtube)

    elif message.text.lower() == "переводчик":
        bot.send_message(message.from_user.id, "Введите слово на русском")
        bot.register_next_step_handler(message, translate)

    elif message.text.lower() == "feedback":
        bot.send_message(message.from_user.id, "Ваш отзыв")
        bot.register_next_step_handler(message, feedback)

    elif message.text.lower() == "разработчик":
        bot.send_message(message.from_user.id, "Разработчик: https://www.instagram.com/v_v_moon?igsh=MTk0ams3ajV5Y3czNA%3D%3D&utm_source=qr")

    else:
        bot.send_message(message.from_user.id, "Бот на стадии разработки:/", reply_markup=buttons.choice_button())




def wiki(message):
    bot.send_message(message.from_user.id, f"https://ru.wikipedia.org/wiki/{message.text}")

def translate(message):
    bot.send_message(message.from_user.id, f"https://translate.yandex.ru/?source_lang=ru&target_lang=en&text={message.text}")

def youtube(message):
    bot.send_message(message.from_user.id, f"https://www.youtube.com/results?search_query={message.text}")

def feedback(message):
    bot.send_message(269578424, message.text)
    bot.send_message(message.from_user.id, "Спасибо за отзыв!")


bot.polling(none_stop=True) #позволяет боту работать 24/7