import random
import matplotlib.pyplot as plt

from book_modu.basic_hist.models import highest_temperature
from book_modu.changed_temperatures_on_my_birthday.models import ChangedTemperaturesOnMyBirthday


class BasicBoxPlot(object):

    def sorted_random_arr(self) -> []:
        arr = []
        [arr.append(random.randint(1, 1000)) for i in range(13)]
        return arr

    def show_boxplot(arr: []):
        plt.boxplot(arr)
        plt.show()

    def show_boxplot_month(month: str):
        plt.boxplot(highest_temperature(month))
        plt.show()

    def show_boxplot_all_month(self):
        birth = ChangedTemperaturesOnMyBirthday()
        birth.read_data()
        arr = birth.data
        month = [[], [], [], [], [], [], [], [], [], [], [], []]
        '''for i in arr:
            if i[-1] != '':
                month[int(i[0].split('-')[1])-1].append(float(i[-1]))'''
        [month[int(i[0].split('-')[1])-1].append(float(i[-1])) for i in arr if i[-1] != '']
        plt.boxplot(month)
        plt.show()

    def show_boxplot_per_date(month: str):
        birth = ChangedTemperaturesOnMyBirthday()
        birth.read_data()
        day = []
        [day.append([]) for i in range(31)]
        [day[int(i[0].split('-')[2])-1].append(float(i[-1])) for i in birth.data if i[-1] != '' if i[0].split('-')[1] == month]
        plt.style.use('ggplot')  # Graph Style
        plt.figure(figsize=(10, 5), dpi=300)  # Graph Size
        plt.boxplot(day, showfliers=False)  # Omit Outlier
        plt.show()
