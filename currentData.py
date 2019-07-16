import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

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
    #k = '15/10/2017'
    browser.get('http://www.squawka.com/football-player-rankings#performance-score#player-stats#german-bundesliga|season-2017/2018#all-teams#all-player-positions#16#40#0#0#90#' + date + '#' + date + '#season#1#all-matches#total#desc#total')
    browser.find_element_by_tag_name('a').send_keys(Keys.END)
    sleep(60)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    divTag = soup.find_all("div", {"id": "main-col"})
    tableTag = divTag[0].find_all('table', {"id": "ranking-stats-table"})
    trTag = tableTag[0].find('tbody').find_all('tr', {"class":"ranking-data-row player"})
    li = []
    for eachRow in trTag:
        di = {}
        di['photoLink'] = eachRow.find('img').get('src')
        #print(di['photoLink'])
        di['name'] = eachRow.find('div', {'class': 'stats-player-name'}).text
        #print(di['name'])
        di['team'] = eachRow.find('td', {'class': 'table-playerteam-field'}).find('div', {'class': 'table-playerteam-info'}).find('div', {'class': 'stats-player-team'}).text.split('-')[1].lstrip()
        #print(di['team'])
        di['match'] = eachRow.find_all('td')[2].text
        di['defence'] = eachRow.find_all('td')[4].text
        di['attack'] = eachRow.find_all('td')[5].text
        di['possesion'] = eachRow.find_all('td')[6].text
        li.append(di)
    if not li:
        #print('Enter')
        return
    #print(li)
    #print('jagan')
    #print(len(li))
