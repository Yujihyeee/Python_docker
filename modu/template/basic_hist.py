import matplotlib.pyplot as plt
import random

from modu.template import ChangedTemperaturesOnMyBirthday


def hist_show():
    plt.hist([1,1,2,3,4,5,6,6,7,8,10])
    plt.show()


def dice_show(count):
    ls = []
    [ls.append(random.randint(1, 6)) for i in range(5)]
    return ls


def show_hist(ls):
    plt.hist(ls, bins=6)
    plt.show()


def highest_temperature(month: str) -> []:
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    arr = []
    '''[print(i) for i in birth.data]
    for i in birth.data:
        if i[-1] != '':
            if i[0].split('-')[1] == '08':
                aug.append(float(i[-1]))'''
    [arr.append(float(i[-1])) for i in birth.data if i[-1] != '' if i[0].split('-')[1] == month]
    return arr


def show_hist_about(arr: [], month: str):
    plt.hist(arr, bins=100, color='red', label=f'Month {month}')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # hist_show()
    # ls = dice_show(1000000)
    # print(ls)
    # show_hist(ls)
    show_hist_about(highest_temperature('01'), month='01')
