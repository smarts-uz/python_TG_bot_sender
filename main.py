from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove
import configs
from configs import *
from keyboards import button_start, get_markup



TOKEN = configs.TOKEN
group_id = configs.Chat_id

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help', 'about', 'history'])
def command_start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    if message.text == '/start':
        msg = f'Здравствуйте {full_name}, для старта нажмите кнопку!'
        bot.send_message(chat_id, msg, reply_markup=button_start())
    elif message.text == '/help':
        msg = f'Здравствуйте {full_name}, за помощью просим обратится к разработчику'
        bot.send_message(chat_id, msg, reply_markup=ReplyKeyboardRemove())
    elif message.text == '/about':
        msg = f'Здесь скоро будет описание...'
        bot.send_message(chat_id, msg, reply_markup=ReplyKeyboardRemove())

@bot.message_handler(regexp='Начать')
def start_command(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Отправьте текст для рассылки в формате обычного сообщения или .txt')
    bot.register_next_step_handler(msg, send_to_group)


def send_to_group(message:Message):
    chat_id = message.chat.id
    if message.text:
        text = message.text
        bot.send_message(group_id, text, reply_markup=get_markup())
        bot.send_message(chat_id, 'Сообщение успешно отправлено✅')
    elif message.photo:
        print(message.photo[0])
        with open('photos/test.jpg', 'wb') as f:
            f.write(message.photo[0].file_id)
        bot.send_message(chat_id, 'done')


bot.infinity_polling()
