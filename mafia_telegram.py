# -*- coding: utf-8 -*-

import telebot
import random
from telebot import types
import time
import sys
import requests
from threading import Thread
import os

with open("token.txt","a+") as f:
    f.close()

with open ("token.txt", 'r') as token_file:
    for line in token_file:
        token = line
        print(token + "123")
    token_file.close()

bot = telebot.TeleBot(token)

def mafia(players):
    try:
        players = int(players)
    except:
        text = "Ты ввёл не число"
        return text

    def maximum_2(a, b):
        if a >= b:
            return [b, a]
        else:
            return [a, b]

    if players > 10:
        roles = random.sample(range(1, players+1), 10)
        mafia = maximum_2(roles[0], roles[1])
        text = f"Мафия - {mafia[0]}, {mafia[1]}\nМаньяк - {roles[2]}\nАдвокат - {roles[3]}\nЛжец - {roles[4]}\nШериф - {roles[5]}\nСержант - {roles[6]}\nПутана - {roles[7]}\nДоктор - {roles[8]}\nСторож - {roles[9]}"
    elif players > 6:
        roles = random.sample(range(1, players+1), 6)
        mafia = maximum_2(roles[0], roles[1])
        text = f"Мафия - {mafia[0]}, {mafia[1]}\nМаньяк - {roles[2]}\nШериф - {roles[3]}\nПутана - {roles[4]}\nДоктор - {roles[5]}"
    elif players > 4:
        roles = random.sample(range(1, players+1), 3)
        mafia = maximum_2(roles[0], roles[1])
        text = f"Мафия - {roles[0]}\nШериф - {roles[1]}\nДоктор - {roles[2]}"
    else:
        text = "Игроков меньше 5, хули ты творишь"

    return text

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, f"👁️ Привет, введи число игроков чтоб порубиться в мафию")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    #bot.send_message(message.chat.id, read_blocked())
    
    text_send = mafia(message.text)
    bot.send_message(message.chat.id, text_send)
    print(message.chat.id)

bot.polling(none_stop=True, interval=0, timeout=500000)