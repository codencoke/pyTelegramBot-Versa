import requests
import lxml.html
from datetime import date
from PIL import Image


def get_request():
    today = date.today()
    year = today.year
    month = today.month
    if month >= 10:
        month = 10
    elif month >= 7:
        month = 7
    elif month >= 4:
        month = 4
    else:
        month = 1
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/253.31 (KHTML, like Gecko) Chrome/10.0.10.27 Safari/253.31'
    }
    resp = requests.get('https://bangumi.tv/anime/browser/airtime/' + str(year) + '-' + str(month) + '?sort=rank',
                        headers=headers)
    resp.encoding = "utf-8"
    tree = lxml.html.fromstring(resp.text)
    return tree


def get_anime_list():
    tree = get_request()
    main_title = 'Top10 ' + tree.xpath('//title')[0].text
    res = main_title + '\n'

    anime_title = tree.xpath("//a[@class='l']")
    anime_rank = tree.xpath("//span[@class='rank']")
    anime_people = tree.xpath("//span[@class='tip_j']")
    n = 10
    for i in range(0, n):
        title = '*' + anime_title[i + 4].text + '*'
        link = 'https://bangumi.tv' + anime_title[i + 4].attrib['href']
        rank = 'Rank: ' + str(anime_rank[i].sourceline)
        people = anime_people[i].text
        res += '[' + str(i + 1) + '.](' + link + ') ' + title + '\n' + rank + ' ' + people + '\n'
    return res


def get_anime_img(num):
    num -= 1
    if num > 9:
        return 'Input Error'
    tree = get_request()
    anime_img = tree.xpath("//img[@class='cover']")
    img_link = 'https:'
    img_link += anime_img[num].attrib['src']
    img = Image.open(requests.get(img_link, stream=True).raw)
    return img
