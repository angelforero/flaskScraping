# -*- coding: utf-8 -*-
"""
Created on Sat May  8 23:46:11 2021

@author: Angel Forero
"""

import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import json

class ScrapingPage:
    
    data = []
    url = "https://www.bloomberg.com/graphics/2019-eliminating-african-swine-fever/"
    tittle = "none"
    transl_table = dict( [ (ord(x), ord(y)) for x,y in zip( u"‘’´“”–-",  u"'''\"\"--") ] )
    
    def __init__(self, ruta):
        self.url = ruta
    
    def setUrl(self,ruta):
        self.url = ruta
        return True
    
    def getUrl(self):
        return self.url
        
    
    def runScraping(self):
        try:
            driver = webdriver.Chrome(os.getcwd() + '/chromedriver')  
            driver.get(self.url)
            time.sleep(3)
            real_soup = BeautifulSoup(driver.page_source, 'html.parser')
            self.tittle = real_soup.find("h1", {"class": "copy-width article-title"}).text
            containers = real_soup.find_all("div", {"class": "copy-width copy-block"})
            
            for eachContainer in containers:
                itemResult = {}
                #print(eachContainer)
                #print(eachContainer.p)
                subtittle = eachContainer.find("div", {"class": "section-hed"})
                if subtittle:
                    itemResult['subtittle'] = subtittle.text.translate( self.transl_table )
                links = eachContainer.find_all("a", href=True)
                if links:
                    itemResult['links'] = [a['href'] for a in links]
                itemResult['text'] = eachContainer.text.translate( self.transl_table )
                self.data.append(itemResult)

            time.sleep(3)
            driver.quit()
            return True
        except Exception as e:
            print(e)
            return False
            
    
    def getJson(self):
        try:
            return json.dumps(self.data, ensure_ascii=False)
        except Exception as e:
            print(e)
            return e
        
    def getNameArticle(self):
        return self.tittle.translate( self.transl_table )