from telebot import types

def choice_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_wiki = types.KeyboardButton('википедия')
    button_youtube = types.KeyboardButton('ютуб')
    button_translate = types.KeyboardButton('переводчик')
    button_feedback = types.KeyboardButton('feedback')
    kb.add(button_wiki, button_youtube, button_translate, button_feedback)
    return kb