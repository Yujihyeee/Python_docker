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
            #  print(f"{str(n_)}위\n Artist : {i.find('a').text}\n Title : {j.find('a').text}")
            self.artists.append(i.find('a').text)
            self.titles.append(j.find('a').text)
        print(self.titles)
        # print(self.artists)

    def insert_dict(self):
        # 방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
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
