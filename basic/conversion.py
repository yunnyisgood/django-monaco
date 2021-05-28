import pandas as pd
class Conversion(object):

    temp = ''
    num = 0
    f = 0.0
    ls = []
    dt = {}
    h = 'hello'
    df = None
    # dp = ()

    def dp_create(self):
        self.dp = tuple(range(1, 11))

    def dp_to_list(self):
        self.dp = list(self.dp)

    def list_to_float(self):
        self.dp = [float (i) for i in self.dp]

    def float_to_num(self):
        self.dp = [int (i) for i in self.dp]

    def list_to_dictionary(self):
        self.dp = [str (i) for i in self.dp]
        print(f'test: {self.dp}')
        for i in range(0, len(self.dp)):
            self.dt[i] = self.dp[i]

    def string_to_tuple(self):
        print(tuple(list(self.h)))

    def tuple_to_list(self):
        self.h = list(self.h)


    def dictionary_to_dataFrame(self):
        values = [str(i) for i in self.dt.values()]  # dictionary의 value값을 list로 변환
        for i in range(0, len(self.dt)):
            self.dt[str(i)] = values  # dictionary의 key값을 str로 변환
        self.df = pd.DataFrame(self.dt)
        print(self.df)


    @staticmethod
    def main():
        c = Conversion()
        while 1:
            menu = input('0.Exit 1.String 2. Num 3. List 4. Dictionary 5.Tuple')
            if menu == '0':
                break
                # 1부터 10까지 요소를 가진 튜플을 생성하시오
            elif menu == '1':
                c.dp_create()
                print(f'create_tuple:{c.dp}')
            #튜플을 리스트로 전환
            elif menu == '2':
                c.dp_to_list()
                print(f'dp_to_list:{c.dp}')
                #리스트를  실수 리스트로 전환
            elif menu == '3':
                c.list_to_float()
                print(f'list_to_float:{c.dp}')
                # 리스트를  정수 리스트로 전환
            elif menu == '4':
                c.float_to_num()
                print(f'float_to_num:{c.dp}')
                # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif menu == '5':
               c.list_to_dictionary()
               print(f'list_to_dictionary:{c.dt}')
                # hello를 튜플로 전환
            elif menu == '6':
                c.string_to_tuple()
                # 6번 튜플을 리스트로 전환하시오
            elif menu == '7':
                c.tuple_to_list()
                print(c.h)
                #5번 딕셔너리를 데이터 프레임으로 전환하시오
            elif menu == '8':
                c.dictionary_to_dataFrame()
            else:
                continue

Conversion.main()


