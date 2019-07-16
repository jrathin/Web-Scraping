import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def start():
    #browser = webdriver.PhantomJS('phantomjs.exe')
    browser = webdriver.Chrome('chromedriver.exe')
    url = 'http://www.footballsquads.co.uk/ger/2017-2018/'
    tag = 'gerbun.htm'
    browser.get(url+tag)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    divTag = soup.find_all("div", {"id": "main"})
    h5Tag = divTag[0].find_all('h5')
    p_list = []
    #print('Enter')
    for i in h5Tag:
        team = i.text
        #print(i.find("a").get("href"))
        browser.get(url+i.find("a").get("href"))
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        divTag = soup.find_all("div", {"id": "main"})
        tableTag = divTag[0].find_all('table')
        trTag = tableTag[0].find('tbody').find_all('tr')
        #print('Enter2')
        for i in range(1,len(trTag)):
            temp = []
            tdTag = trTag[i].find_all('td')
            #print(tdTag)
            try:
                if tdTag[1].text:
                    temp.append(tdTag[1].text)
                    temp.append(tdTag[2].text)
                    temp.append(tdTag[3].text)
                    temp.append(team)
                    p_list.append(temp)
            except:
                break
        '''for i in range(len(p_list)):
            print(p_list[i])
        '''
    return(p_list)

