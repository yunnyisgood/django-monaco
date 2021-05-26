from bs4 import BeautifulSoup
import requests

class Bugs3(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    class_name = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    title_ls = []
    artist_ls = []
    dict = {}

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    # def set_class_name(self, class_name):
    #     self.class_name = class_name

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        for i in soup.find_all("p", {"class": self.class_name[1]}):
            self.title_ls.append(f'{i.find("a").text}')
        for i in soup.find_all("p", {"class": self.class_name[0]}):
            self.artist_ls.append(f'{i.find("a").text}')

    def insert_title_dict(self):
        # 제목을 key, 가수를  value로

        # 방법 1
        for i in range(0, len(self.title_ls)): # len(list[]) -> list 배열의 길이를 출력함
            self.dict[self.title_ls[i]] = self.artist_ls[i]
            print(self.dict)

        # 방법 2
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]
            print(self.dict)

        # 방법 3
        for i, j in zip(self.title_ls, self.artist_ls):
            self.title_ls[i] = self.artist_ls[j]


    @staticmethod
    def main():
        bugs = Bugs3()
        while 1:
            menu = int(input('0.Exit 1.Input 2.Read 3.Read2'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.set_url(input('Detail')) # wl_ref=M_contents_03_01
            elif menu == 2:
                bugs.class_name.append("title")
                bugs.class_name.append("artist")
                bugs.get_ranking()
            elif menu == 3:
                bugs.class_name.append("title")
                bugs.class_name.append("artist")
                bugs.insert_title_dict()
            else:
                print('Wrong Number')
                continue
Bugs3.main()
