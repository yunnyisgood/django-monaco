'''
구구단 프로그램은 단을 입력받아서, 입력받은 1~9의 곱을 출력하는 어플리케이션
'''

class Gugudan(object):

    dan = 0
    dict = {}

    def print_selected_dan(self):
        # 반복문 for문 안의 for문
        # 구구단 세로 출력
        print("구구단 세로 출력")
        for i in range(1, 10):
            if i == self.dan:
                print(f'{i}단')
                for j in range(1, 10):
                    print(f'{i}X{j} = {i * j}')

    def print_horizontal(self):
        # 구구단 가로 출력 => end='\t' f부분 이후에 넣으면 할 수 있다,,,
        print("구구단 가로 출력")
        for j in range(1, 10):
            for i in range(1, 10):
                    print(f'{j}X{i} = {i * j}', end='\t')

    def print_all_dan(self):
        # 구구단 전체 출력
        print("구구단 전체 출력")
        for i in range(1, 10):
            print(f'{i}단')
            for j in range(1, 10):
                print(f'{i} X {j} = {i*j}')

    def print_dict_dan(self):
        d = self.dict
        for i in range(1, 10):
            d[i] = self.dan * i
        print('딕셔너리 출력')
        print(d)
        for k in d.keys():
            print(f'{self.dan}*{k} = {d.get(k)}')

    # 구구단  dictionary에 넣기
    def test(self):
        for i in range(1, 10):
            # dict['name'] = 'maria' -> 이렇게 선언하는 것과 똑같은 방식
            self.dict[i] = self.dan * i  #  여기서 key값은 self.dan, value는 i -> self.dict 정의
        print('딕셔너리 출력')
        print(self.dict)
        for k in self.dict.keys():
            print(f'{self.dan}*{k} = {self.dict.get(k)}')



    @staticmethod
    def main():
        g = Gugudan()
        while 1:
            menu = int(input('0.Exit 1.Input and Print 2. all dan 3.Input dan with dict'))
            if menu == 0:
                break
            elif menu == 1:
                g.dan = int(input('1~10 사이의 수를 입력하세요'))
                # input은 화면상에서 입력을 받는 메소드이기 때문에 staticmethod안에 두어야 한다.
                # 이 떄 입력받는 인스턴스를 default 생성자에 의해 생성한다.
                g.print_selected_dan()
                g.print_horizontal()
            elif menu == 2:
                g.print_all_dan()

            elif menu == 3:
                g.dan = int(input('1~10 사이의 수를 입력하세요'))
                g.print_dict_dan()


Gugudan.main()

