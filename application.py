# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:28:25 2021

@author: Angel Forero
"""

from flask import Flask, jsonify
from ScrapingPage import ScrapingPage

application = Flask(__name__)

scrap = ScrapingPage("https://www.bloomberg.com/graphics/2019-eliminating-african-swine-fever/")

# Testing Route
@application.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

@application.route('/set/url/<string:urlnew>', methods=['GET'])
def setUrl(urlnew):
    booleanResult = scrap.setUrl(urlnew)
    return booleanResult

@application.route('/runscraping', methods=['GET'])
def runScrap():
    booleanResult = scrap.runScraping()
    return jsonify({'success': booleanResult})

@application.route('/get/tittle', methods=['GET'])
def getTittle():
    return jsonify({'tittle': scrap.getNameArticle()})

@application.route('/get/json', methods=['GET'])
def getJson():
    return scrap.getJson()

@application.route('/get/url', methods=['GET'])
def getUrl():
    return jsonify({'url': scrap.getUrl()})


if __name__ == '__main__':
    application.run(debug=True, port=5000)
    #scrap = ScrapingPage("https://www.bloomberg.com/graphics/2019-eliminating-african-swine-fever/")
