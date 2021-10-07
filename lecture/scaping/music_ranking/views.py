from lecture.menu.models import print_menu
from lecture.scaping.melon.models import MusicRanking

if __name__ == '__main__':
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