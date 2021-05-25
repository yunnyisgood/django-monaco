from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):

    url = ''



    @staticmethod
    def ranking(url, class_name):
        soup = BeautifulSoup(urlopen(url), 'lxml')
        count = 0
        print('<<Artist Ranking>>')
        for i in soup.find_all(name='p', attrs=({"class":class_name[0]})):
            count += 1
            print(f'{str(count)} 위')
            print(f'{class_name[0]}: {i.find("a").text}')
        print('<<Title Ranking>>')
        for i in soup.find_all(name='p', attrs=({"class":class_name[0]})):
            count += 1
            print(f'{str(count)} 위')
            print(f'{class_name[0]}: {i.find("a").text}')



    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input('0. Exit 1. Input URL\n 2.Ranking'))
            if menu == 0:
                break

            elif menu == 1:
                url = input('url 입력하세요')
                # BugsMusic(input('url을 입력하세요'))

            elif menu == 2:
                bugs.ranking(url, ["artist", "title"])
            else:
                print('다시 입력해주세요')
                continue

#    https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
BugsMusic.main()