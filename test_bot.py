# -- coding: utf-8 --

import telebot 
import config
import sqlite3
import time
import random

from telebot import types

import sqlite

bot = telebot.TeleBot()#your token

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    rand_button = types.KeyboardButton(text="Рандомный факт")
    categ_button = types.KeyboardButton(text="Категории")
    keyboard.add(rand_button, categ_button)
    bot.send_message(message.chat.id, "Привет, я бот, который дает факты", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def facts(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомный факт':
            categ = random.randint(1, 3)
            fact = random.randint(1, 3)
            if categ == 1:
                name_tabel = 'chemistry'
            if categ == 2:
                name_tabel = 'history'
            if categ == 3:
                name_tabel = 'physics'
            bot.send_message(message.chat.id, sqlite.fact_return(name_tabel, fact))
        elif message.text == 'Категории':
            keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
            cat1 = types.KeyboardButton(text="Химия")
            cat2 = types.KeyboardButton(text="Физика")
            cat3 = types.KeyboardButton(text="История")
            cat4 = types.KeyboardButton(text="Категории")
            exit = types.KeyboardButton(text="Назад")
            keyboard1.add(cat1, cat2, cat3, cat4, exit)
            bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=keyboard1)

        elif message.text == 'Привет':
            start (message)

        elif message.text == 'Химия':
            fact = random.randint(1, 3)
            bot.send_message(message.chat.id, sqlite.fact_return('chemistry', fact))
	
        elif message.text == 'Физика':
            fact = random.randint(1, 3)
            bot.send_message(message.chat.id, sqlite.fact_return('physics', fact))

        elif message.text == 'История':
            fact = random.randint(1, 1)
            bot.send_message(message.chat.id, sqlite.fact_return('history', fact))

        elif message.text == 'Назад':
            keyboard = types.ReplyKeyboardMarkup()
            rand_button = types.KeyboardButton(text="Рандомный факт")
            categ_button = types.KeyboardButton(text="Категории")
            keyboard.add(rand_button, categ_button)
            bot.send_message(message.chat.id, reply_markup=keyboard)

        else:
            bot.send_message(message.chat.id,'К сожалению, я Вас не понимаю. Попробуйте еще раз или обратитесь за помощью по следующей команде /help')

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(0.1)

