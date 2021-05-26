class Vector_test2(object):

    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'name':'홍', 'age':'30세'}

    def create(self):
        self.dt.update(input("수정할 key"))


    @staticmethod
    def main():
        dictionary = Vector_test2
        while 1:
            menu = int(input('0.Exit\n 1.Create\n 2.Read\n 3.Update\n 4.Delete'))
            if menu == 0:
                break
            elif menu == 1:
                dictionary.dt.update(input('Input'))
            elif menu == 2:
                print(f'dt: {dictionary.dt}')
            elif menu == 3:
                edit_key = input('수정하고자하는 이름을 입력하세요')
                edit_value = input('value 입력: ')
                val = input('value 입력: ')
                dictionary.dt[key] = val


                for i, j in enumerate(dictionary.dt):
                    if j == dictionary.dt:
                        del dictionary.dt[i]
                        dictionary.dt.update(edit_info)
            elif menu == 4:
                del_name = input('삭제할 이름을 입력하세요')
                for i, j in enumerate(dictionary.dt):
                    if j == dictionary.dt:
                        del dictionary.dt[i]
                        print('삭제 되었습니다.')

            else:
                print('wrong input')
                continue

Vector_test2.main()
