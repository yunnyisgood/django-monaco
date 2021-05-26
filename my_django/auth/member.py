class Member(object):
    # Default 생성자가 인스턴스를 생성하는 방법
    id = ''
    pw = ''
    name = ''
    email = ''

    # # 파라미터 생성자가 인스턴스를 생성하는 방법
    # def __init__(self, id, pw, name, email):
    #     self.id = id
    #     self.pw = pw
    #     self.name = name
    #     self.email = email

    def to_string(self):
        return f'아이디: {self.id}, 비밀번호: {self.pw}, 이름: {self.name}, 이메일: {self.email}'

    @staticmethod
    def main():
        member = []
        while 1:
            menu = int(input('0.Exit 1.Create 2.Read 3.Update 4.Delete'))
            if menu == 0:
                break
            elif menu == 1:
                member.id = input('id')



                member.append(Member(input('id'), input('pw'), input('name'), input('email')))
            elif menu == 2:
                for i in member:
                    print(f'회원가입된 유저: {i.to_string()}')
            elif menu == 3:
                update_member = input(f'수정할 이름을 입력하세요: ')
                update_info = Member(input('id'), input('pw'), input('name'), input('email'))
                for i in enumerate(member):
                    if i.name == member.name:
                        del member[i]
            elif menu == 4:
                delete_member = input(f'삭제할 이름을 입력하세요: ')
                for i in enumerate(member):
                    if i.name == member.name:
                        del member[i]
                        print('삭제 완료 되었습니다.')

Member.main()




Member.main()


