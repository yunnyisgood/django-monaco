from bs4 import BeautifulSoup
import requests

class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')# url 읽기
        count = 0
        print("<<Title Ranking>>")
        for i in soup.find_all("div", {"class":self.class_name[0]}):  # div 클래스에서 class_name[0]을 찾아라
            count += 1
            print(str(count))
            print(f'{i.find("a").text}') # 찾아서 a 태그 안의 text를 또 찾아서 print해
        print("<<Artist Ranking>>")
        for i in soup.find_all("div", {"class": self.class_name[1]}):  # div 클래스에서 class_name[1]을 찾아라
            count += 1
            print(str(count))
            print(f'{i.find("a").text}')

    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = int(input('0.Exit\n 1. Input URL\n 2. Get Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                melon.set_url(input('스크래핑할 날짜 입력'))  # '2021052511'
            elif menu == 2:
                melon.class_name.append("ellipsis rank01")
                melon.class_name.append("ellipsis rank01")
                melon.get_ranking()

            else:
                print('Wrong number')
                continue

Melon.main()