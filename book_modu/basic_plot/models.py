import matplotlib.pyplot as plt


class BasicPlot(object):
    """
    list 값은 y 축이고, x축은 0부터 1까지 자동으로 증가한다.
    """
    def plot_show(self):
        plt.title("plotting")
        plt.plot([10, 20, 30, 40])
        plt.show()

    """
    첫번째 list가 x축, 두번째 리스트가 y 축이다.
    """
    def plot_two_list_show(self):
        plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
        plt.show()

    def plot_three_list_show(self):
        plt.title("legend")
        plt.plot([10, 20, 30, 40], color="purple", label="asc")
        plt.plot([40, 30, 20, 10], color="black", label="desc")
        plt.legend()
        plt.show()

    def plot_color(self):
        plt.title("color")
        plt.plot([10, 20, 30, 40], color="skyblue", label="skyblue")
        plt.plot([40, 30, 20, 10], color="pink", label="pink")
        plt.legend()
        plt.show()

    def plot_linestyle(self):
        plt.title("linestyle")
        plt.plot([10, 20, 30, 40], color="r", linestyle = "--", label = "dashed")
        plt.plot([40, 30, 20, 10], color="g", ls=":", label="dotted")
        plt.legend()
        plt.show()

    def plot_scatter(self):
        plt.title("marker")
        plt.plot([10, 20, 30, 40], "r.", label="circle")
        plt.plot([40, 30, 20, 10], "g^", label="triangle up")
        plt.legend()
        plt.show()
