from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):

    url = ''
    class_name = []

#   @staticmethod  -> 아래 self.url을 사용하면서 메모리에 할당됨 -> staticmethod가 아니어야 함.
    def ranking(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        count = 0
        print('<<Artist Ranking>>')
        for i in soup.find_all(name='p', attrs=({"class":self.class_name[0]})):
            count += 1
            print(f'{str(count)} 위')
            print(f'{self.class_name[0]}: {i.find("a").text}')
        print('<<Title Ranking>>')
        for i in soup.find_all(name='p', attrs=({"class":self.class_name[1]})):
            count += 1
            print(f'{str(count)} 위')
            print(f'{self.class_name[1]}: {i.find("a").text}')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input('0. Exit 1. Input URL\n 2.Ranking'))
            if menu == 0:
                break

            elif menu == 1:
                bugs.url = input('url 입력하세요')

            elif menu == 2:
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.ranking()
                # bugs.ranking(["artist", "title"])  # 리스트에 담기
            else:
                print('다시 입력해주세요')
                continue

#    https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
BugsMusic.main()