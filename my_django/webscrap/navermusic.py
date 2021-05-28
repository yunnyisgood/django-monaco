from bs4 import BeautifulSoup
import requests
class Navermusic(object):

    url = 'https://vibe.naver.com/chart/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}

    def set_url(self, range):
        self.url = requests.get(f'{self.url}{range}', headers=self.headers).text

    def get_ranking(self):
        print("1")
        soup = BeautifulSoup(self.url, 'lxml')
        # print(f'2 스크래핑 결과 사이즈 : {len(soup.find_all("div", {"class":self.class_name[0]}))}')
        for i in soup.find_all("div", {"class":self.class_name[0]}):
            print("3")
            self.title_ls.append(f'{i.find("a").text}')
            print(f'title<<<{self.title_ls}')
        for i in soup.find_all("span", {"class":self.class_name[1]}):
            print("4")
            self.artist_ls.append(f'{i.find("a").text}')
            print(f'artist<<< {self.artist_ls}')
        print("5")

    def get_dict(self):
        for i in range(0, len(self.title_ls)):
            print("5")
            self.dict[self.title_ls[i]] = self.artist_ls[i]
        print(self.dict)

    @staticmethod
    def main():
        naver = Navermusic()
        while 1:
            menu = input('0.Exit 1. URL 2. Get ranking 3. Get dict ')
            if menu == '0':
                break
            elif menu == '1':
                naver.set_url(input('total / domestic'))
                print(naver.url)
            elif menu == '2':
                naver.class_name.append("title_badge_wrap")
                naver.class_name.append("inner")
                naver.get_ranking()
            elif menu == '3':
                naver.class_name.append("title_badge_wrap")
                naver.class_name.append("inner")
                naver.get_dict()
            else:
                print('wrong number')
                continue
Navermusic.main()


