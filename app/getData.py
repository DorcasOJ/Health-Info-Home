import requests
from bs4 import BeautifulSoup
import os, random, time
import pandas as pd


# To get home page health quote        
def quote_list():
    with open('data/health_quotes.txt', 'r') as f:
        quotes = f.readlines()
    quotes = [ i.strip() for i in quotes]
    quotes = [i.replace('"', '') for i in quotes]
    #for quote in quotes:
        #time.sleep(seconds)
    return quotes


# To get news for home page and for Insight page
def get_news(api):
    url = f'http://newsapi.org/v2/top-headlines?country=ng&category=health&apiKey={api}'
    try:
        out = requests.get(url)
        t = out.json()['articles']
        t = [(i['title'], i['url']) for i in t]
        t = [i for i in t if len(i[0].split()) < 25]
        t = [t[0], random.choice(t[1:])]
    except:
        t = 'Error Loading page'

    #channel

    try:
        channel = requests.get('https://www.channelstv.com/category/health')
        soup = BeautifulSoup(channel.content, 'lxml')

        ch_strings = [i.string for i in soup.findAll('div', {'class', 'panel-txt'})]
        ch_a = [ i.find('a', href= True) for i in soup.findAll('div', {'class': 'cat_page'})]

        ch_url = []
        for j in ch_a:
            sent = []
            for i in str(j):
                if i != '>':
                    sent.append(i)
                if i == '>':
                    break
            ch_url.append(''.join(sent[9:-1]))
        ch_news = [[i.strip(), j.strip()] for i, j in zip(ch_strings, ch_url)]
        ch_choice = [ch_news[0], random.choice(ch_news[1:]) ]
    except:
        ch_choice = 'Error Loading page'


    #punch
    try:
        punch = requests.get('https://punchng.com/topics/health/')
        soup = BeautifulSoup(punch.content, 'lxml')

        first =  soup.findAll('h3', {'class': 'entry-title'})
        second = [i.findAll('a', href= True) for i in first]
        p_strings = [n.string for i in second for n in i]
        second_f = [str(n)[9:] for i in second for n in i]
        p_url = []
        for ht in second_f:
            sent = []
            for i in ht:
                if i != '>':
                    sent.append(i)
                if i == '>':
                    break
            p_url.append(''.join(sent[:-1]))

        p_news = [[i.strip(), j.strip()] for i, j in zip(p_strings, p_url)]
        p_choice = [p_news[0] ,random.choice(p_news[1:])]
    except:
        p_choice = 'Error Loading page'

    return t, ch_choice, p_choice


# To get health data to  graph
class CovidData:
    def __init__(self):
        print('\nLoading Covid Data Class')
        try:
            print('Getting covid overall info from NCDC...')
            page = requests.get('https://covid19.ncdc.gov.ng')
            self.soup = BeautifulSoup(page.content, 'lxml')
            print('Successful!')
        except:
            print('Failed! Using existing data')
            self.soup = None
        self.pop = None
        self.covid_overall = None
        self.covid_data = None

    def get_covid_overall_info(self):
        if self.soup is not None:
            self.covid_overall = pd.DataFrame(['Samples Tested','Comfirm Cases', 'Active Cases', 'Discharged Cases', 'Death'], columns = ['Info'])
            self.all_span = [i.string for i in self.soup.find_all('span')]
            self.span_all = [str(i).replace(',', '') for i in self.all_span if i]
            self.data = [int(i) for i in self.span_all if i.isdigit()]
            self.covid_overall['Data'] = self.data
            self.covid_overall.to_csv('data/covid_overall.csv', index= False)
        else:
            self.covid_overall = None
            
    def get_covid_overall_data(self):
        self.get_covid_overall_info()
        if self.covid_overall is None:
            return self.soup
        return self.covid_overall
        
  