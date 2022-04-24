import requests
import lxml.html


def rm_symbols(s):
    i = 0
    for i in range(len(s)):
        if '0' <= s[i] <= '9':
            break
    j = i
    for j in range(i, len(s)):
        if (s[j] < '0' or s[j] > '9') and s[j] != '.':
            break
    return s[i:j]


def fix_len(s):
    j = 7 - len(s)
    for i in range(0, j):
        s += '  '
    return s


def get_price():
    resp = requests.get('http://www.icbc.com.cn/icbcdynamicsite/charts/goldtendencypicture.aspx')
    resp.encoding = "utf-8"
    tree = lxml.html.fromstring(resp.text)
    table = tree.xpath('//tr[@class="style_text"]/td')
    price_in = table[2].text
    price_out = table[3].text
    price_in = fix_len(rm_symbols(price_in))
    price_out = fix_len(rm_symbols(price_out))
    gold = '*黄金：*\n | 买：' + price_in + '| 卖：' + price_out

    resp = requests.get('https://www.boc.cn/sourcedb/whpj/')
    resp.encoding = "utf-8"
    tree = lxml.html.fromstring(resp.text)
    table = tree.xpath('//tr/td')
    eur = 56
    jpy = 96
    usd = 208
    eur_str = '\n' + table[eur].text + '\n | 买：' + fix_len(table[eur + 1].text) + '| 卖：' + fix_len(
        table[eur + 3].text)
    jpy_str = '\n' + table[jpy].text + '\n | 买：' + fix_len(table[jpy + 1].text) + '| 卖：' + fix_len(
        table[jpy + 3].text)
    usd_str = '\n' + table[usd].text + '\n | 买：' + fix_len(table[usd + 1].text) + '| 卖：' + fix_len(
        table[usd + 3].text)
    money = '\n*汇率：*' + eur_str + jpy_str + usd_str
    return gold + money
