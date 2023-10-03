import json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def button_start():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Начать')
    markup.add(btn)
    return markup


def get_markup():
    with open('files/Mrk.json', 'r', encoding='UTF-8') as file:
        a = file.read()
    mrk_dict = json.loads(a)
    list_of_keyboard = mrk_dict['inline_keyboard'][0]
    markup = InlineKeyboardMarkup()
    for i in list_of_keyboard:
        markup.add(InlineKeyboardButton(i['text'], url=i['url']))
    markup.row_width = 2
    return markup








