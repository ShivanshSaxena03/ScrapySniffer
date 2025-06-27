import requests

from bs4 import BeautifulSoup

import pprint
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
sup = BeautifulSoup(res.text,'html.parser')
sup2 = BeautifulSoup(res2.text,'html.parser')
links = (sup.select('.titleline a'))
links2 = (sup2.select('.titleline a'))
subtext = (sup.select('.subtext'))
subtext2 = (sup2.select('.subtext'))
mega_link = links+links2
mega_sub = subtext+subtext2

def sortbyvotes(li):
    return sorted(li,key=lambda x:x["votes"])
def custom_links(links,subtext):
    li= []
    for idx in range(min(len(links), len(subtext))):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',""))
            if points>99:
                li.append({'title':title,'links':href,"votes" : points})
    return sortbyvotes(li)

pprint.pprint(custom_links(mega_link,mega_sub))
