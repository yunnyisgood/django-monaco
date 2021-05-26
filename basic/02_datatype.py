# *****************
# --- Data Type ---
# *****************
'''
Python has Five standard types
scalar
    Numbers : int, float, complex
    String : str
vector : List, Tuple, Dictionary, Set
hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])
'''
# List CRUD Example
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']
# Create: ls 에 '100'을 추가 Create
ls.append(100)
print(f'Create:{ls}')
# Read: ls 의 목록을 출력
print(f'Read:{ls}')
# Update: ls와 tinyls 의 결합
print(f'Update:{ls+tinyls}')
# Delete: ls 에서 786을 제거
del ls[1]  # 삭제 방법 1
ls.remove(1) # 삭제 방법 2
print(f'Delete:{ls}')


# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
# Read: tp 의 목록을 출력
# Update: tp와 tinytp 의 결합
# Delete: tp 에서 786을 제거
# dictionary CRUD Example
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍', '30세'}
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
# Read: dt 의 목록을 출력
# Update: dt와 tinydt 의 결합
# Delete: dt 에서 'abcd' 제거