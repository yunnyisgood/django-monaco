from bs4 import BeautifulSoup
import urllib.request
class Bugs2(object):

    url = ''
    class_name = []
    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}


    def set_url(self, time):
        self.url = f'https://www.melon.com/chart/index.htm?dayTime={time}'

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_ranking(self):
        req = urllib.request.Request(self.url, headers=self.hdr)
        url = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(url, 'html.parser')
        print("<<Title Ranking>>")
        for i in soup.find_all("div", {"class":self.class_name[0]}):
            print(f'{i.find("a").text}')
        print("<<Artist Ranking>>")
        for i in soup.find_all("div", {"class":self.class_name[1]}):
            print(f'{i.find("a").text}')

    @staticmethod
    def main():
        b = Bugs2()
        while 1:
            menu = int(input('0, 1-input, 2-output'))
            if menu == 1:
                b.set_url(input('time 예) 2021052515'))
            elif menu == 2:
                b.class_name.append('ellipsis rank01')
                b.class_name.append('ellipsis rank02')
                b.get_ranking()
Bugs2.main()