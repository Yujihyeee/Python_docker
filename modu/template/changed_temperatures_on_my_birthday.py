import csv
import pandas as pd
import matplotlib.pyplot as plt
'''
next()는 두가지 포맷으로 사용된다. 
function 구조로 사용되면 header 만 리턴한다.
consumer 구조로 사용하면 data 에서 header 를 제거한다.
row[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)] 최고기온은 -1 이다.
data: [] = list()는 list 타입의 data 를 list() 로 초기화시키는 것이다.
단, 한 메소드 내에서만 사용하면 로컬에서 초기화하고,
data : [] = None
def save_highest_temperatures(self):
    data = list()
그러나. 여러 메소드에서 사용하면 필드에서 초기화한다. 예제는 다음과 같다.
data : [] = list()
'''


class ChangedTemperaturesOnMyBirthday():
    data: [] = list()
    highest_temperatures: [] = list()

    def preprocessing(self):
        self.read_data()
        self.save_highest_temperature()
        self.visualize_data()
        self.extract_date_data()

    def read_data(self):
        data = csv.reader(open('data/seoul.csv', 'rt', encoding='UTF-8'))
        next(data)
        # print([i for i in data])
        self.data = data

    def show_highest_temperature(self):
        # print([i[-1] for i in self.data])
        return [i[-1] for i in self.data]

    def save_highest_temperature(self):
        [self.highest_temperatures.append(float(i[-1])) for i in self.data if i[-1] != '']
        # print(self.highest_temperatures)
        # print(f'총 {len(self.highest_temperatures)} 개')

    def visualize_highest_temperature(self):
        plt.plot(self.highest_temperatures, 'r')
        plt.figure(figsize=(20, 2))
        plt.show()

    def highest_temperature_my_birthday(self):
        high = []  # 최고기온
        low = []  # 최저기온

        for i in self.data:
            if i[-1] != '' and i[-2] != '':
                if 1995 <= int(i[0].split('-')[0]):
                    if i[0].split('-')[1] == '05' and i[0].split('-')[2] == '18':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))

        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일의 기온 변화 그래프')
        plt.plot(high, 'hotpink', label='high')
        plt.plot(low, 'skyblue', label='low')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    this = ChangedTemperaturesOnMyBirthday()
    this.read_data()
    # this.show_highest_temperature()
    # this.save_highest_temperature()
    # this.visualize_highest_temperature()
    this.highest_temperature_my_birthday()