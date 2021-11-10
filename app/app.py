from flask import Flask, redirect, render_template, request, Markup, jsonify
from os import path, walk
import random, time
import requests
from getData import quote_list, get_news, CovidData
import pandas as pd, numpy as np

app = Flask(__name__)

api_key = 'f69b33c1639044108e76fc692e1bd9d6'


@app.route('/')
def home_page():
    # get quotes
    quotes = quote_list()

    #get news from api
    news, chan, pun = get_news(api_key)
    news_dict = {'news':news, 'chan':chan, 'pun': pun}
    
    # get covid overall data
    covid_data = CovidData()
    covid_overall = covid_data.get_covid_overall_data()
    if covid_overall is None:
        covid_overall = pd.read_csv('data/covid_overall.csv')
    covid_overall_dict = {'labels': covid_overall.Info.values, 'values': covid_overall.Data.values}
    colour_dict = {'Confirmed Cases':'rgb(16, 145, 231)','Active Cases':'goldenrod', 'Discharged Cases':'rgb(43, 136, 43)', 'Deaths':'rgb(233, 16, 16)'}
        

    return render_template('home.html', health_quote = random.choice(quotes), 
    news_dict = news_dict, covid_overall_dict = covid_overall_dict, 
    colour_dict = colour_dict)

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.cache = {}
    app.run(debug = True, use_reloader = True, use_debugger= True) #port = 8005
