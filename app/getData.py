import requests
from bs4 import BeautifulSoup
import os, random, time
import pandas as pd


# To get home page health quote        
def quote_list():

    with open('./app/data/health_quotes.txt', 'r') as f:
        quotes = f.readlines()
    quotes = [ i.strip() for i in quotes]
    quotes = [i.replace('"', '') for i in quotes]
    return quotes
