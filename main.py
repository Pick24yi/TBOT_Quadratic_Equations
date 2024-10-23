import telebot
import math


bot = telebot.TeleBot('') # Токен бота


# Вступление бота (реакция на команду /start и /help)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет! Я бот, созданный для решения полных квадратных уравнений.
Прошу, следуй инструкциям!
Полное квадратное уравнение - это уравнение вида ax²+bx+c=0.
Для продолжения напиши "Ок".
Важно: десятичные дроби записывать через точку.\
""")
    bot.register_next_step_handler(message, get_text_messages_1) # Переход к функции get_text_messages_1

@bot.message_handler(content_types=['text'])
def get_text_messages_1(msg1):
    bot.send_message(msg1.from_user.id, text='a = ?')
    bot.register_next_step_handler(msg1, get_text_messages_2) # Переход к функции get_text_messages_2

@bot.message_handler(content_types=['text'])
def get_text_messages_2(msg2):
    global a
    a = float(msg2.text)
    bot.send_message(msg2.from_user.id, text='b = ?')
    bot.register_next_step_handler(msg2, get_text_messages_3) # Переход к функции get_text_messages_3

@bot.message_handler(content_types=['text'])
def get_text_messages_3(msg3):
    global b
    b = float(msg3.text)
    bot.send_message(msg3.from_user.id, text='c = ?')
    bot.register_next_step_handler(msg3, get_text_messages_4) # Переход к функции get_text_messages_4

@bot.message_handler(content_types=['text'])
def get_text_messages_4(msg4):
    global c
    c = float(msg4.text)

    #Сбор данных закончился, дальше идут вычисления корней

    discr = b ** 2 - 4 * a * c
    bot.send_message(msg4.from_user.id, text="D = %.2f" % discr)
    if discr > 0:                                               #Вариант с 2 корнями
        discr = b ** 2 - 4 * a * c
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        bot.send_message(msg4.from_user.id, text="x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:                                            #Вариант с 1 корнем
        x = -b / (2 * a)
        bot.send_message(msg4.from_user.id, text="x = %.2f" % x)
    else:                                                       #Вариант без корней
        bot.send_message(msg4.from_user.id, text="Корней нет")


bot.polling(none_stop=True, interval=0)  #Команда, позволяющая боту всегда принимать соо от пользователя(во время работы самого бота очевидно)