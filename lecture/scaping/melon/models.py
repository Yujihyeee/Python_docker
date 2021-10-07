from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
import requests
import pandas as pd


class MelonMusic(object):

    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers= self.headers)
        soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'lxml')
        _ = 0
        artists = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        titles = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        for i, j in zip(artists, titles):
            _ += 1
            print(f"{str(_)}위\n Artist : {i.find('a').text}\n Title : {j.find('a').text}")
