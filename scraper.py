import requests
from bs4 import BeautifulSoup as bfs
import pprint

# res = requests.get('https://news.ycombinator.com/news?P=1')
# soup = bfs(res.text, 'html.parser')
# link = soup.select('.titlelink')
# subtext = soup.select('.subtext')
# https://news.ycombinator.com/news?p=1


def sorted_hn_list(hn_list):
    return sorted(hn_list, key=lambda k: k['score'], reverse=True)


def my_hacker_new(link, subtext):
    hn_list = list()
    for item in range(len(link)):
        score = subtext[item].select('.score')
        if len(score):
            score = score[0].getText()  # string
            score = int(score[:score.index(' ')])
            if score > 100:
                hn_list.append({'title': link[item].getText(
                ), 'score': score, 'Link': link[item].get('href', None)})
    return hn_list


full_list = list()
for i in range(3):
    res = requests.get('https://news.ycombinator.com/news?P=' + str(i))
    soup = bfs(res.text, 'html.parser')
    link = soup.select('.titlelink')
    subtext = soup.select('.subtext')
    full_list = my_hacker_new(link, subtext) + full_list
    full_list = sorted_hn_list(full_list)

pprint.pprint(full_list)
