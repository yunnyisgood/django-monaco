from bs4 import BeautifulSoup
class Bs_demo(object):

    html_doc = ''

    def __str__(self):
        return f'html_doc: {self.html_doc}'

    @staticmethod
    def main():
        bs = Bs_demo()
        while 1:
            menu = int(input('0. 종료\n 1. 자동입력\n 2. 출력\n 3. 제목만 출력'))
            if menu == 0:
                break
            elif menu == 1:
                bs.html_doc = """<html><head><title>The Dormouse's story</title></head>
                                <body>
                                <p class="title"><b>The Dormouse's story</b></p>
                                
                                <p class="story">Once upon a time there were three little sisters; and their names were
                                <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                                and they lived at the bottom of a well.</p>
                                
                                <p class="story">...</p>
                                """
            elif menu == 2:
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.prettify())
            elif menu == 3:
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.p)
                print(soup.a['href'])
                print(soup.find_all('p'))
                print(soup.find(id="link2"))

                # print(soup.title)
                # print(soup.title.name)   # title
                # print(soup.title.string)  # The Dormouse's story
                # print(soup.title.parent.name)  # head

            else:
                print('다시 입력하세요')
                continue

Bs_demo.main()
