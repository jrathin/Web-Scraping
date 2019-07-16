import requests
from bs4 import BeautifulSoup
from datetime import datetime

'''
class Scrap:

    def __init__(self, url):

        self.url = url

    def start(self):

        self.htmlPage = requests.get(self.url)
        print(self.htmlPage.text)
        self.soup = BeautifulSoup(self.htmlPage.content, "html.parser")
        self.divTag = self.soup.find_all("div", {"id": "main-col"})
        #print(self.divTag[0])
        self.tableTag = self.divTag[0].find_all('table', {"id": "ranking-stats-table"})
        #print(self.tableTag)
        self.trTag = self.tableTag[0].find('tbody').find_all('tr', {"style-class":"ranking-data-row-player"})
        #find_all('tr', {'class': 'ranking-data-row player'})
        print(self.trTag)

url = 'http://www.squawka.com/football-player-rankings#performance-score#player-stats#german-bundesliga|season-2017/2018#all-teams#all-player-positions#16#40#0#0#90#18/08/2017#13/10/2017#season#1#all-matches#total#desc#total'
obj = Scrap(url)
obj.start()
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''
#browser = webdriver.PhantomJS('phantomjs.exe')
browser = webdriver.Chrome('chromedriver.exe')
date = ''
date = str(datetime.now().day)
temp = ''
temp = str(datetime.now().month)    
if len(date) == 1:
    date = '0' + date
if len(temp) == 1:
    temp = '0' + temp
date += '/' + temp + '/' + str(datetime.now().year)
browser.get('http://www.squawka.com/football-player-rankings#performance-score#player-stats#german-bundesliga|season-2017/2018#all-teams#all-player-positions#16#40#0#0#90#18/08/2017#'+date+'#season#1#all-matches#total#desc#total')
'''
'''pd = 60

while pd:
    elem = browser.find_element_by_tag_name('a')
    elem.send_keys(Keys.PAGE_DOWN)
    pd = pd-1
'''

def start():
    #browser = webdriver.PhantomJS('phantomjs.exe')
    browser = webdriver.Chrome('chromedriver.exe')
    date = ''
    date = str(datetime.now().day)
    temp = ''
    temp = str(datetime.now().month)    
    if len(date) == 1:
        date = '0' + date
    if len(temp) == 1:
        temp = '0' + temp
    date += '/' + temp + '/' + str(datetime.now().year)
    browser.get('http://www.squawka.com/football-player-rankings#performance-score#player-stats#german-bundesliga|season-2017/2018#all-teams#all-player-positions#16#40#0#0#90#18/08/2017#'+date+'#season#1#all-matches#total#desc#total')
    browser.find_element_by_tag_name('a').send_keys(Keys.END)
    import time
    time.sleep(100)

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    divTag = soup.find_all("div", {"id": "main-col"})
    tableTag = divTag[0].find_all('table', {"id": "ranking-stats-table"})
    trTag = tableTag[0].find('tbody').find_all('tr', {"class":"ranking-data-row player"})
#tdTag = trTag[0].find_all('td')
#l = trTag[0].find('td', {'class': 'table-playerteam-field'}).find('div', {'class': 'table-playerteam-info'}).find('div', {'class': 'stats-player-team'}).text
#print(l)
    li = []
    for eachRow in trTag:
        '''di = {}
        di['photoLink'] = eachRow.find('img').get('src')
        print(di['photoLink'])
        di['name'] = eachRow.find('div', {'class': 'stats-player-name'}).text
        print(di['name'])
        di['team'] = eachRow.find('td', {'class': 'table-playerteam-field'}).find('div', {'class': 'table-playerteam-info'}).find('div', {'class': 'stats-player-team'}).text.split('-')[1].lstrip()
        print(di['team'])
        di['match'] = eachRow.find_all('td')[2].text
        di['defence'] = eachRow.find_all('td')[4].text
        di['attack'] = eachRow.find_all('td')[5].text
        di['possesion'] = eachRow.find_all('td')[6].text
        '''
        temp = []
        temp.append(eachRow.find('div', {'class': 'stats-player-name'}).text)
        temp.append(eachRow.find('img').get('src'))
        li.append(temp)
    return(li)

'''a = start()
for i in a:
    print(i)
'''
