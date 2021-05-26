class Vector_test(object):

    ls = ['abcd', 786, 2.23, 'john', 70.2]

    def create(self):
        self.ls.append(input("Input"))

    def read(self):
        return f'{self.ls}'

    def replace(self):
        name = input('Input')
        for i, j in enumerate(list.ls):
            if j == name:
                del list.ls[i]

    @staticmethod
    def main():
        list = Vector_test()
        while 1:
            menu = int(input('0. Exit\n 1.Create\n 2.Read\n 3.Update\n 4.Delete\n '))
            if menu == 0:
                break
            elif menu == 1:
                # list.ls.append(input("Input"))
                list.create()
            elif menu == 2:
                for i in list.ls:
                   print(f'{list.ls[i]}')
                # print(list.ls)
            elif menu == 3 :
                list.replace()
                edit_update = input('새로운 요소를 입력하세요')
                list.ls.append(edit_update)
            elif menu == 4 :
                list.replace()
            else:
                print('Wrong Input')
                continue

Vector_test.main()
