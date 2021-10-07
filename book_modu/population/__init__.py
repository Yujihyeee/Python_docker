from lecture.menu import print_menu
from modu.template.basic_plot import plot_show, plot_two_list_show, plot_three_list_show, plot_color, plot_linestyle, plot_scatter
from modu.template.changed_temperatures_on_my_birthday import ChangedTemperaturesOnMyBirthday

if __name__ == '__main__':
    while 1:
        menu = print_menu(['exit', 'Plot Show', 'plot_two_list_show', ' plot_three_list_show', 'plot_color',
                           'plot_linestyle', 'plot_scatter', 'ChangedTemperaturesOnMyBirthday'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_three_list_show()
        elif menu == 4:
            plot_color()
        elif menu == 5:
            plot_linestyle()
        elif menu == 6:
            plot_scatter()
        elif menu == 7:
            ChangedTemperaturesOnMyBirthday().processing()