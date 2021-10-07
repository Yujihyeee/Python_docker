from book_modu.basic_hist.models import BasicHist

if __name__ == '__main__':
    # hist_show()
    # ls = dice_show(1000000)
    # print(ls)
    # show_hist(ls)
    b = BasicHist()
    b.show_hist_about(b.highest_temperature('01'), month='01')