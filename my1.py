import telebot
from telebot import types
import random
import sqlite3
import constants

#2081710670:AAFNbaHUKUSM649ryTaVPamHhKNgxh-NYXY

bot = telebot.TeleBot('2081710670:AAFNbaHUKUSM649ryTaVPamHhKNgxh-NYXY')

# база данных пользовательских id
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id, 'http://www.kvn.ru/public/uploads/files/5/201392/mode2600x400_201909211859528d2692ee28.jpg', caption='*НУ ПРИВЕЕЕЕЕЕЕТ!!!*', parse_mode='Markdown')
    bot.send_message(message.chat.id, "Держи список всех команд:\n/team - дает тебе название команды\n/help - вызывает справку")


@bot.message_handler(commands = ['team'])
def team(message):
    random_team0 = constants.random_man() + " из " + constants.random_place()
    random_team1 = constants.random_prilag() + ' ' + constants.random_man()
    random_team2 = constants.random_team()
    random_team3 = 'Сборная ' + constants.random_place()
    random_team4 = constants.random_man() + " с " + constants.random_such()
    random_team5 = constants.random_man() + " без " + constants.random_bez_chego()
    random_team6 = [random_team0, random_team1, random_team2, random_team3, random_team4, random_team5]
    random_team = lambda: random.choice(random_team6)
    bot.send_message(message.from_user.id, '⚡️Перед вами команда КВН ' + '*"' + random_team() + '"*' + ' будем знакомы!⚡️', parse_mode='Markdown')
    # добавляем клавиатуру
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Клево 👍', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Атстой, давай по новой', callback_data='no')
    keyboard.add(key_no)
    #bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDJGVhdT4HJShhi4VKocAhQrjC-cUsTAACogEAAonq5QeUHcFTKsUlfSEE")
    bot.send_message(message.chat.id, 'Как тебе название?', reply_markup=keyboard)
    # добавляем голосовалку
    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == 'yes':
            bot.send_photo(message.chat.id, 'https://sun9-9.userapi.com/impg/Z9IMB7t_kREA-Z-4ci_ih_ae7QEX6i4rvB3CPw/i6Ca0r6wJIE.jpg?size=900x600&quality=96&sign=420f14ba154809de89f24434ca7f5af1&type=album', caption=constants.random_otvet())
            bot.send_message(message.chat.id, "Поделись ботом с другом @team_name_KVN_bot")
        elif call.data == 'no':
            team(message)
            #bot.send_message(message.chat.id, '/team')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Держи список всех команд:\n/team - дает тебе название команды\n/help - вызывает справку")

@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def get_text_messages(message):
    if message.text == "иди нахуй":
        bot.send_message(message.chat.id, "Сам иди, долбоеб")
    else:
        bot.send_photo(message.chat.id, 'https://sun9-25.userapi.com/impg/nb1_C9yu919T4maUScmJQWhdu6dnbLaRQ-GREg/wKNMLrNtGI0.jpg?size=500x257&quality=96&sign=2c0e698a0e024da3f46e636c47ce450f&type=album', caption="Я тебя не понимаю. Напиши /help.", parse_mode='Markdown')
        #bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
