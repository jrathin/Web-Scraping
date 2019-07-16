import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def injuryScrap():
    url = 'https://www.online-betting.me.uk/germany-bundesliga-injuries-and-suspensions.php'
    #browser = webdriver.PhantomJS('phantomjs.exe')
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    h3Tag = soup.find_all('div', {'id': 'main-content', 'class': 'col-md-9'})[0].find('div', {'class': 'injuries-table-container'}).find_all('h3')
    tableTag = soup.find_all('div', {'id': 'main-content', 'class': 'col-md-9'})[0].find('div', {'class': 'injuries-table-container'}).find_all('table', {'class': 'injurytable'})
    li = []
    index = 0
    for eachTable in tableTag:
        trTag = eachTable.find('tbody').find_all('tr')
        di = {}
        tempList = []
        for eachTr in range(1, len(trTag)):
            tempDict = {}
            temp = []
            tdTag = trTag[eachTr].find_all('td')
            #tempDict['typeOfInjury'] = tdTag[0].get('class')
            #tempDict['player'] = tdTag[1].text
            #tempList.append(tempDict)
            temp.append(tdTag[0].get('class')[0])
            temp.append(tdTag[1].text)
            li.append(temp)
        #di[h3Tag[index].text] = (tempList)
        #index += 1
        #li.append(di)
    return(li)
    '''for i in li:
        print(i)
        print('\n----------------------------------------------\n')

injuryScrap()
'''
