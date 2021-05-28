import pandas as pd
class Conversion(object):


    df = pd.DataFrame()
    # dp = ()

    @staticmethod
    def dp_create() -> ():
        # 여기서 프로퍼티(self)를 사용하지 않는다 -> 객체 메소드가 아닌 staticmethod
        return (1, 2, 3, 4, 5, 6, 7, 8, 9)

    @staticmethod
    def dp_to_list(dp) -> []:
        return list(dp)

    @staticmethod
    def list_to_float(dp) -> []: # 리스트를 실수로 변환
        return [float(dp[i]) for i in range(0, len(dp))]

    @staticmethod
    def float_to_num(dp) -> []:
        return [int(dp[i]) for i in range(0, len(dp))]

    @staticmethod
    def list_to_dictionary(dp) -> {}:
        return dict(zip([str(i) for i in dp], [str(i) for i in dp]))

    @staticmethod
    def string_to_tuple(h)-> ():
        return tuple(list(h))

    @staticmethod
    def tuple_to_list(h) -> []:
        return list(h)

    # @staticmethod
    def dictionary_to_dataFrame(dt):
        return pd.DataFrame.from_dict(dt, orient='index')




    @staticmethod
    def main():
        c = Conversion()
        temp = ''
        num = 0
        f = 0.0
        ls = []
        dt = {}
        h = 'hello'

        while 1:
            menu = input('0.Exit 1.String 2. Num 3. List 4. Dictionary 5.Tuple')
            if menu == '0':
                break
                # 1부터 10까지 요소를 가진 튜플을 생성하시오
            elif menu == '1':
                 dp = c.dp_create()
                 print(dp)
            # 튜플을 리스트로 전환
            elif menu == '2':
                dp = c.dp_to_list(dp)
                print(f'dp_to_list:{dp}')
                #리스트를  실수 리스트로 전환
            elif menu == '3':
                dp = c.list_to_float(dp)
                print(f'list_to_float:{dp}')
                # 리스트를  정수 리스트로 전환
            elif menu == '4':
                dp = c.float_to_num(dp)
                print(f'float_to_num:{dp}')
                # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif menu == '5':
               c.list_to_dictionary(dp)
               print(f'list_to_dictionary:{dt}')
                # hello를 튜플로 전환
            elif menu == '6':
                h = c.string_to_tuple(h)
                print(h)
                # 6번 튜플을 리스트로 전환하시오
            elif menu == '7':
                h = c.tuple_to_list(h)
                print(h)
                #5번 딕셔너리를 데이터 프레임으로 전환하시오
            elif menu == '8':
                df = c.dictionary_to_dataFrame(pd.DataFrame(dt))
            else:
                continue

Conversion.main()


