import requests
import os
import telebot

bot = telebot.TeleBot('6138326503:AAGPQfC0a4FOHUgw32pXSe2b3AIrHdZilo8')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="فحص coins", callback_data="check")
    button2 = telebot.types.InlineKeyboardButton(text="رشق متابعين", callback_data="followers")
    button3 = telebot.types.InlineKeyboardButton(text="JHENMمطور", url="https://t.me/bbdbio")
    button4 = telebot.types.InlineKeyboardButton(text="SD مطور", url="https://t.me/bbdbio")
    markup.add(button1, button2)
    markup.add(button3, button4)
    bot.reply_to(message, "مرحبًا! أنا بوت فحص ورشق متابعين انستا .\n\nإذا كنت تريد فحص coins الخاصة بك، اضغط على زر فحص coins. أو اضغط على زر رشق متابعين لتفعيل الخدمة المدفوعة.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "check":
        user_id = call.message.chat.id
        bot.send_message(chat_id=call.message.chat.id, text="قم بإرسال ايديك ليتم فحصه.")
        bot.register_next_step_handler(call.message, process_coin_count_step)
    elif call.data == "followers":
        bot.send_message(chat_id=call.message.chat.id, text="أهلا بك في قسم رشق متابعين المدفوع، لتفعيل هذه الخدمة يرجى التواصل مع المطور على الرابط التالي سعر التفعيل ١$ اسيا : @WVKWV")

def process_coin_count_step(message):
    try:
        user_id = int(message.text)
        coin_count = get_likes(user_id)
        bot.send_message(chat_id=message.chat.id, text=f'{user_id} ===> {coin_count} ')
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text="حدث خطأ أثناء الفحص، يرجى إرسال ايدي صحيح.")
        print(e)

def get_likes(user_id):
    res = requests.get(f'http://instaup.marsapi.com/get_likes/shop/daily_coins?user_id={user_id}').json()
    coin = int(res['return']['coins'])
    return coin

bot.polling()