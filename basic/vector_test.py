class Vector_test(object):

    # 필드의 프로퍼티
    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']

    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')

    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍', '30세'}


    def ls_create(self):
        print(self.ls.append(input("Input")))

    def ls_read(self):
        print(self.ls)
        # return f'{self.ls}'

    def ls_update(self):
        # Update: ls와 tinyls 의 결합
        print(self.ls.extend(self.tinyls))
        print(self.ls+self.tinyls)

    def ls_delete(self):
        # Delete: ls 에서 786을 제거
        print(self.ls.remove(1))

    def tp_create(self):
        self.tp = self.tp+ (100,)  # 원래는 변경안됨-> 덮어쓰기

    def tp_read(self):
        print(self.tp)

    def tp_merge(self):
        print(self.tp+self.tinytp)

    def tp_delete(self):
        print("Impossible")
        # Delete: tp 에서 786을 제거
        # 변경 불가

    def dt_create(self):
        # Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
        self.dt['tom'] = 100  # [ ]인 이유 => key값들이 list로 묶여져 있기 때문에
        print(self.dt)

    def dt_update(self):
        # Update: dt와 tinydt 의 결합
        print(self.dt.update(self.tinydt))

    def dt_delete(self):
        # Delete: dt 에서 'abcd' 제거
        del self.dt[0]
        print(self.dt)

    @staticmethod
    def main():
        vector = Vector_test()
        while 1:
            menu = int(input('0. Exit\n 1.Create\n 2.Read\n 3.Update\n 4.Delete\n '))
            if menu == 0:
                break
            elif menu == 1:
                print(vector.ls_create())
            elif menu == 2:
                print(vector.ls_read())
            elif menu == 3 :
                print(vector.ls_update())
            elif menu == 4 :
                print(vector.ls_delete())
            elif menu == 5:
                print(vector.tp_create())
            elif menu == 6:
                print(vector.tp_read())
            elif menu == 7:
                print(vector.tp_merge())
            elif menu == 8:
                print(vector.tp_delete())
            elif menu == 8:
                print(vector.tp_delete())
            elif menu == 8:
                print(vector.tp_delete())
            elif menu == 8:
                print(vector.tp_delete())

            else:
                continue

Vector_test.main()
