import telebot
from pycbrf.toolbox import ExchangeRates
from telebot import types
from datetime import datetime
bot = telebot.TeleBot("Ваш токен")
now = datetime.now()
date_time = now.strftime("%Y-%m-%d")
rates = ExchangeRates(date_time)
USD = str(rates['USD'].value)
EUR = str(rates['EUR'].value)
CNY = str(rates['CNY'].value)
BYN = str(rates['BYN'].value)
CZK = str(rates['CZK'].value)
UAH = str(rates['UAH'].value)
CAD = str(rates['CAD'].value)

@bot.message_handler(commands=['help'])
def print_help(message):
    keyboardHelp = types.ReplyKeyboardMarkup()
    restart = types.KeyboardButton('/start')
    val_enc = types.KeyboardButton('/val_enc')
    val_calc = types.KeyboardButton('/val_calc')
    keyboardHelp.add(val_calc,val_enc,restart)
    bot.send_message(message.chat.id, "Выбирайте валюты или нажмите на кнопку помощи", reply_markup=keyboardHelp)
    message_text = 'Вот, что умеет этот бот:\n' \
                    + '/help - отображает список доступных команд\n' \
                    + '/val_enc - отображает кодировки валют\n'\
                    + '/start - курс валют\n'\
                    + '/val_calc - конвертер'
    bot.send_message(message.chat.id, message_text)
@bot.message_handler(commands=['val_enc'])
def Valute_encording(message):
    message_text = 'Здесь представлены некоторые валюты:\n'\
                        + 'USD - Доллар США\n'\
                        + 'EUR - Евро\n'\
                        + 'BYN - Белорусский рубль\n'\
                        + 'CNY - Китайский юань женьминьби\n'\
                        + 'CAD - Канадский доллар\n'\
                        + 'CZK - Чешская крона\n'
    bot.send_message(message.chat.id, message_text)

@bot.message_handler(commands=['start'])
def start(message):
    keyboardVal = types.ReplyKeyboardMarkup()
    CZK = types.KeyboardButton('CZK')
    USD = types.KeyboardButton('USD')
    EUR = types.KeyboardButton('EUR')
    CNY = types.KeyboardButton('CNY')
    BYN = types.KeyboardButton('BYN')
    CAD = types.KeyboardButton('CAD')
    UAH = types.KeyboardButton('UAH')
    help = types.KeyboardButton('/help')
    keyboardVal.add(USD, EUR, CNY, BYN, CZK, CAD, UAH,help)
    bot.send_message(message.chat.id, "Выбирайте валюты или нажмите на кнопку помощи", reply_markup=keyboardVal)
    bot.register_next_step_handler(message, Valute_rate)

def Valute_rate(message):
    if message.text == "USD":
        bot.send_message(message.chat.id, "*💰Курс USD: *"+ USD + ' *₽*',parse_mode="Markdown")
        bot.register_next_step_handler(message, Valute_rate)
    elif message.text == "EUR":
        bot.send_message(message.chat.id, "*💰Курс EUR: *"+ EUR + ' *₽*',parse_mode="Markdown")
        bot.register_next_step_handler(message, Valute_rate)
    elif message.text == "CNY":
        bot.send_message(message.chat.id,  "*💰Курс CNY: *"+ CNY + ' *₽*',parse_mode="Markdown")
        bot.register_next_step_handler(message, Valute_rate)
    elif message.text == "BYN":
        bot.send_message(message.chat.id, "*💰Курс BYN: *" + BYN + ' *₽*', parse_mode="Markdown")
        bot.register_next_step_handler(message, Valute_rate)
    elif message.text == "CZK":
        bot.send_message(message.chat.id, "*💰Курс CZK: *" + CZK + ' *₽*', parse_mode="Markdown")
        bot.register_next_step_handler(message, Valute_rate)
    elif message.text == "CAD":
        bot.send_message(message.chat.id, "*💰Курс CAD: *" + CAD + ' *₽*', parse_mode="Markdown")
        bot.register_next_step_handler(message, Valute_rate)
    elif message.text == "UAH":
        bot.send_message(message.chat.id, "*💰Курс UAH: *" + UAH + ' *₽*', parse_mode="Markdown")
        bot.register_next_step_handler(message, Valute_rate)
