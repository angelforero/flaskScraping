# -*- coding: utf-8 -*-
"""
Created on Sun May  9 02:02:33 2021

@author: Angel Forero
"""

#import ScrapingPage
from ScrapingPage import ScrapingPage

scrap = ScrapingPage("https://www.bloomberg.com/graphics/2019-eliminating-african-swine-fever/")


def test_name():
    assert scrap.getNameArticle == "none"

def test_sraping():
    assert scrap.scrapingPage == True

def test_set_url():
    assert scrap.setUrl("https://www.bloomberg.com/graphics/2019-eliminating-african-swine-fever/") == True

def test_json(): 
    assert scrap.scrap.getJson()