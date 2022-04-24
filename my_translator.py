import requests
import os


def yandex_translate(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = dict(
        key=os.environ['YANDEX_API'],
        text=text,
        lang='zh',
    )

    resp = requests.get(url=url, params=params)
    data = resp.json()
    res = data['text'][0]
    return res
