from local_process import local_process

local_process()

import os
import telebot
import random
import time
from my_anime import get_anime_list, get_anime_img
from my_weibo import weibo_search, weibo_news
from my_zhihu import get_zhihu_hot
from my_translator import yandex_translate
from my_stock import get_price

# from keep_alive import keep_alive
# keep_alive()

bot_key = os.environ['API_KEY']
bot = telebot.TeleBot(bot_key, parse_mode='MARKDOWN')


@bot.message_handler(commands=['help'])
def show_help(msg):
    func_info = [
        '当前功能：',
        '\n/help - 查看帮助',
        '\n/hi - 打招呼',
        '\n/jrrp - 今日人品',
        '\n/dice - 撒骰子',
        '\n/rand - 随机数（用法：/rand 1,999）',
        '\n/trans - 翻译（用法：/trans fuck）',
        '\n/anime - 获取本季热播新番列表',
        '\n/stock - 查看金融信息',
        '\n/weibo1 - 女厕热搜',
        '\n/weibo2 - 女厕新闻',
        '\n/zhihu - 男厕热搜'
    ]
    help_info = ''.join(func_info)
    bot.send_message(msg.chat.id, help_info)


@bot.message_handler(regexp='^/debug')
def print_debug_info(msg):
    print(msg)


@bot.message_handler(commands=['hi'])
def greeting(msg):
    username = '@' + msg.from_user.username + ' '
    n = 5
    random.seed(time.time())
    num = random.randint(1, n)
    greet = ''
    if num == 1:
        greet = 'hi'
    if num == 2:
        greet = 'yo fucker'
    if num == 3:
        greet = 'sup man'
    if num == 4:
        greet = 'hey bitch'
    if num == 5:
        greet = 'run run run!'
    bot.send_message(msg.chat.id, username + greet)


@bot.message_handler(commands=['dice'])
def dice(msg):
    bot.send_dice(msg.chat.id)


@bot.message_handler(regexp='^/trans')
def get_translate(msg):
    text = msg.text[6:]
    if len(text) <= 0:
        bot.send_message(msg.chat.id, 'Input Error')
        return
    bot.send_message(msg.chat.id, '(Yandex Translation)\n' + yandex_translate(text))


@bot.message_handler(commands=['anime'])
def bangumi_list(msg):
    res = get_anime_list()
    bot.send_message(msg.chat.id, res)


@bot.message_handler(regexp='/anime(10|[1-9])')
def bangumi_img(msg):
    num = int(msg.text[6:])
    img = get_anime_img(num)
    bot.send_photo(msg.chat.id, img)


@bot.message_handler(commands=['stock'])
def get_stock(msg):
    res = get_price()
    bot.send_message(msg.chat.id, res)


@bot.message_handler(regexp='^/rand')
def get_rand(msg):
    text = msg.text[5:]
    first_num = ''
    second_num = ''
    i = 0
    flag = False
    for i in range(len(text)):
        if text[i] == ' ':
            continue
        if text[i] == ',':
            flag = True
            i += 1
            break
        if (text[i] > '9' or text[i] < '0') and text[i] != '-':
            bot.send_message(msg.chat.id, 'Input Error')
            return
        first_num += text[i]
    if not flag:
        bot.send_message(msg.chat.id, 'Input Error')
        return
    for j in range(i, len(text)):
        if text[j] == ' ':
            continue
        if (text[j] > '9' or text[j] < '0') and text[j] != '-':
            bot.send_message(msg.chat.id, 'Input Error')
            return
        second_num += text[j]
    a = int(first_num)
    b = int(second_num)
    if a > b:
        c = a
        a = b
        b = c
    random.seed(time.time())
    res = random.randint(a, b)
    bot.send_message(msg.chat.id, 'Random Number: ' + str(res))


@bot.message_handler(commands=['jrrp'])
def jrrp(msg):
    user_id = msg.from_user.id
    date = int((msg.date + 28800) / 86400)
    random.seed(date)
    rp = (user_id * date + random.randint(0, 99)) % 101
    username = '@' + msg.from_user.username
    if rp == 100:
        status = '(卧槽)'
    elif rp >= 80:
        status = '(大吉)'
    elif rp >= 60:
        status = '(吉)'
    elif rp >= 50:
        status = '(小吉)'
    elif rp >= 40:
        status = '(小凶)'
    elif rp >= 20:
        status = '(凶)'
    else:
        status = '(大凶)'
    bot.send_message(msg.chat.id, username + ' 今日人品：' + str(rp) + '/100 *' + status + '*')


@bot.message_handler(commands=['weibo1'])
def weibo1(msg):
    res = weibo_search()
    bot.send_message(msg.chat.id, res)


@bot.message_handler(commands=['weibo2'])
def weibo2(msg):
    res = weibo_news()
    bot.send_message(msg.chat.id, res)


@bot.message_handler(commands=['zhihu'])
def zhihu(msg):
    res = get_zhihu_hot()
    bot.send_message(msg.chat.id, res)


bot.polling()
