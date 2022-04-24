import requests
import lxml.html


def get_zhihu_hot():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/253.31 (KHTML, like Gecko) Chrome/10.0.10.27 Safari/253.31'
    }
    resp = requests.get('https://zhihu.com/billboard', headers=headers)
    tree = lxml.html.fromstring(resp.text)
    titles = tree.xpath('//div[@class="HotList-itemTitle"]')
    res = '*知乎热榜 Top10*'
    n = 10
    for i in range(0, n):
        res += '\n' + str(i + 1) + '. ' + titles[i].text
    return res
