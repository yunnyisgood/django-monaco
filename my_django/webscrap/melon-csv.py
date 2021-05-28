import pandas as pd
from bokeh.colors.groups import orange
from bs4 import BeautifulSoup
import requests

class Melon(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')# url 읽기
        for i in soup.find_all("div", {"class":self.class_name[0]}):
            self.title_ls.append(f'{i.find("a").text}')
        for i in soup.find_all("div", {"class": self.class_name[1]}):
            self.artist_ls.append(f'{i.find("a").text}')

    def get_dict(self):
        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
            print(self.dict)

    def dict_to_dataFrame(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient="index")
        # orient = columns면 키를 열의 레이블로
        # orient = index면 키를 행의 레이블로 설정한다.
        print(self.df)

    def dataFrame_to_csv(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep=',', na_rep='Nan')


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
                melon.class_name.append("ellipsis rank02")
                melon.get_ranking()
            elif menu == 3:
                melon.class_name.append("ellipsis rank01")
                melon.class_name.append("ellipsis rank02")
                melon.get_dict()
            elif menu == 4:
                melon.dict_to_dataFrame()
            elif menu == 5:
                melon.dataFrame_to_csv()

            else:
                print('Wrong number')
                continue

Melon.main()