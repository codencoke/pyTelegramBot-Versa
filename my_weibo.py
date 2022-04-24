import requests
import lxml.html


def weibo_search():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/253.31 (KHTML, like Gecko) Chrome/10.0.10.27 Safari/253.31',
        'cookie': 'SUB=_2Aasjci93910NxqwJRmP8czWasf125vsa8ieKjRgHAJZC5a8s2KOJlks2963201e9KkQ622_1cjYGw5tESxmkexXUXX1; SUBP=0033WrSXqPxfM72-Ws9jqgMa99962P9D9W5p7_KnzgonUY1ccYWSYpZc'
    }
    resp = requests.get('https://s.weibo.com/top/summary?cate=realtimehot', headers=headers)
    tree = lxml.html.fromstring(resp.text)
    titles = tree.xpath('//td[@class="td-02"]/a')
    n = 11
    res = '*微博热搜榜 Top10*'
    for i in range(0, n):
        res += '\n' + str(i) + '. ' + titles[i].text
    return res


def weibo_news():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'cookie': 'SUB=_2Aasjci93910NxqwJRmP8czWasf125vsa8ieKjRgHAJZC5a8s2KOJlks2963201e9KkQ622_1cjYGw5tESxmkexXUXX1; SUBP=0033WrSXqPxfM72-Ws9jqgMa99962P9D9W5p7_KnzgonUY1ccYWSYpZc'
    }
    resp = requests.get('https://s.weibo.com/top/summary?cate=socialevent', headers=headers)
    tree = lxml.html.fromstring(resp.text)
    titles = tree.xpath('//td[@class="td-02"]/a')
    n = 11
    res = '*微博热搜榜 Top10*'
    for i in range(0, n):
        res += '\n' + str(i) + '. ' + titles[i].text
    return res
