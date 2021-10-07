from lecture.scaping.bugs_music.models import BugsMusic

if __name__ == '__main__':
    BugsMusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
                      f'chartdate={"20211007"}&charthour={"15"}').scrap()
