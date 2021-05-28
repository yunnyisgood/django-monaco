from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup


class Movie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    classes = ''
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    # driver = 'C://Program Files//Google//Chrome//chromedriver' 이렇게 표기할수도 있다.

    movie_ranking = []
    movie_dict = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser') # 여기서는 'lxml' 사용불가
        all_div = soup.find_all("div", {"class":self.classes})
        self.movie_ranking = [{i.find("a").text} for i in all_div]
        print(self.movie_ranking)
        driver.close()

    def get_dict(self):
        for i in range(0, len(self.movie_ranking)):
            self.movie_dict[i] = self.movie_ranking
        print(self.movie_dict)

    def get_dataFrame(self):
        self.df = pd.DataFrame(self.movie_dict)
        print(self.df)

    def get_csv(self):
        path = './data/naverMusic.csv'
        self.df.to_csv(path, sep=',', na_rep='Nan')


if __name__ == '__main__':
    movie = Movie()
    movie.classes = input('클래스를 입력하세요')  # tit3
    movie.scrap()
    movie.get_dict()
    movie.get_dataFrame()
    movie.get_csv()
