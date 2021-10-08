import pandas as pd


class Crime(object):

    def exec(self):
        df = pd.read_csv('./data/police_positions.csv', encoding='UTF-8', thousands=',')
        #  df['crime'] = df['살인 발생'] + df['강도 발생'] + df['강간 발생'] + df['절도 발생'] + df['폭력 발생']
        #  df['arrest'] = df.groupby(df['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'])
        print(df['crime'])
        df['crime'].to_csv('data/cctv_pop.csv')


if __name__ == '__main__':
    c = Crime()
    c.exec()


    '''
    self.crime_columns = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']  # Nominal
    self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']  # Nominal
    '''