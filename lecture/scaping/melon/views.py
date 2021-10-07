from lecture.scaping.melon.models import MelonMusic

if __name__ == '__main__':
    MelonMusic('https://www.melon.com/chart/index.htm?dayTime=2021072112').scrap()