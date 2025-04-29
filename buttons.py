from telebot import types

def choice_button():
    kb = types.ReplyKeyboardMarkup()
    button_wiki = types.KeyboardButton('Wiki')
    kb.add(button_wiki)
    return kb