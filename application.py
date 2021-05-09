# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:28:25 2021

@author: USUARIO
"""

from flask import Flask, jsonify
from ScrapingPage import ScrapingPage

app = Flask(__name__)

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

@app.route('/set/url/<string:urlnew>', methods=['GET'])
def setUrl(urlnew):
    booleanResult = scrap.setUrl(urlnew)
    return booleanResult

@app.route('/runscraping', methods=['GET'])
def runScrap():
    booleanResult = scrap.runScraping()
    return jsonify({'success': booleanResult})

@app.route('/get/tittle', methods=['GET'])
def getTittle():
    return jsonify({'tittle': scrap.getNameArticle()})

@app.route('/get/json', methods=['GET'])
def getJson():
    return scrap.getJson()

@app.route('/get/url', methods=['GET'])
def getUrl():
    return jsonify({'url': scrap.getUrl()})


if __name__ == '__main__':
    scrap = ScrapingPage("https://www.bloomberg.com/graphics/2019-eliminating-african-swine-fever/")
    app.run(debug=True, port=5000)