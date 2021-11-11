from flask import Flask, redirect, render_template, request, Markup, jsonify
from os import path, walk
import random, time
import requests
from getData import quote_list, CovidData
import pandas as pd, numpy as np

app = Flask(__name__)


@app.route('/')
def home_page():
    # get quotes
  
    quotes = quote_list()    

    return render_template('home.html', health_quote = random.choice(quotes))

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.cache = {}
    app.run(debug = True, use_reloader = True, use_debugger= True) #port = 8005
