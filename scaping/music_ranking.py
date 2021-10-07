import requests
import pandas as pd
from bs4 import BeautifulSoup

from menu.models import print_menu


class MusicRanking(object):
    domain = ''
    query_string = ''
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    tag_name = ''
    fname = ''
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        # print(f'Crawling HTML is {self.html}')

    def get_ranking(self):
        soup = BeautifulSoup(self.html, 'lxml')
        n_ = 0
        artists01 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[0]})
        titles01 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[1]})
        for i, j in zip(artists01, titles01):
            n_ += 1
            #print(f"{str(n_)}위\n Artist : {i.find('a').text}\n Title : {j.find('a').text}")
            self.artists.append(i.find('a').text)
            self.titles.append(j.find('a').text)
        print(self.titles)
        # print(self.artists)

    def insert_dict(self):
        '''
        # 방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        '''
        # 방법 3
        for i, j in enumerate(self.titles):
            self.dict[j] = self.artists[i]
        print(self.dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


def main():
    mr = MusicRanking()
    while 1:
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', ' Bugs Output', 'Melon Output',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210722&charthour=15'
            mr.set_html()
        elif menu == 2:
            mr.domain = 'https://www.melon.com/chart/index.htm?'
            mr.query_string = 'dayTime=2021072216'
            mr.set_html()
        elif menu == 3:
            mr.tag_name = 'p'
            mr.class_name.append('artist')
            mr.class_name.append('title')
            mr.get_ranking()
        elif menu == 4:
            mr.tag_name = 'div'
            mr.class_name.append('ellipsis rank02')
            mr.class_name.append('ellipsis rank01')
            mr.get_ranking()
        elif menu == 5:
            mr.insert_dict()
        elif menu == 6:
            mr.dict_to_dataframe()
        elif menu == 7:
            mr.df_to_csv()


if __name__ == '__main__':
    main()