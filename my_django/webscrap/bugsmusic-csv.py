from bs4 import BeautifulSoup
import requests
import pandas as pd
class Bugs3(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    class_name = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text


    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        for i in soup.find_all("p", {"class": self.class_name[0]}):
            self.title_ls.append(f'{i.find("a").text}')
        for i in soup.find_all("p", {"class":self.class_name[1]}):
            self.artist_ls.append(f'{i.find("a").text}')

    def insert_title_dict(self):
        # 제목을 key, 가수를  value로
        # 방법 1
        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
            print(self.dict)
        #
        # 방법 2
        # for i, j in enumerate(self.title_ls):
        #     self.dict[j] = self.artist_ls[i]
        #     print(self.dict)
        #
        # # 방법 3
        # for i, j in zip(self.title_ls, self.artist_ls):
        #     self.title_ls[i] = self.artist_ls[j]

    def dict_to_dataFrame(self):
        values = [str(i) for i in self.dict.values()]
        for i in range(0, len(self.dict)):
            self.dict[str(i)] = values
        self.df = pd.DataFrame.from_dict(self.dict)
        print(self.df)


    def dataFrame_to_csv(self):
        path = './data/bugs2.csv'
        self.df.to_csv(path, sep=',', na_rep='Nan')




    @staticmethod
    def main():
        bugs = Bugs3()
        while 1:
            menu = int(input('0.Exit 1.Input 2.Read 3.Read2 4.dict_to_dataFrame'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.set_url(input('Detail')) # wl_ref=M_contents_03_01
            elif menu == 2:
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == 3:
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.insert_title_dict()
            elif menu == 4:
                bugs.dict_to_dataFrame()
            elif menu == 5:
                bugs.dataFrame_to_csv()
            else:
                print('Wrong Number')
                continue
Bugs3.main()
