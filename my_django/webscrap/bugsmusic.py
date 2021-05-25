from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):

    url = ''



    @staticmethod
    def ranking(something, soup):
        count = 0
        for i in soup.find_all(name='p', attrs=something):
            count += 1
            print(f'{str(count)} 위')
            print(f'{something}: {i.find("a").text}')



    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input('0. Exit 1. Input URL\n 2.Ranking'))
            if menu == 0:
                break

            elif menu == 1:
                bugs.url = input('url을 입력하세요')
                # BugsMusic(input('url을 입력하세요'))

            elif menu == 2:
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                print('<<Artist Ranking>>')
                bugs.ranking("artist", soup)
                print('<<Title Ranking>>')
                bugs.ranking("title", soup)

            else:
                print('다시 입력해주세요')
                continue

#    https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
BugsMusic.main()