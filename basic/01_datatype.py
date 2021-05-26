# *******
# --- Data Type ---
# *******

'''
Python has Five standard Type
Scalar
    Numbers: int, float, complex
    String : str
Vector: :List, Tuple, Dictionary, Set
-> 여기서 List, Tuple은 Set 구조. Dictionary, Set은 hash구조

'''
#
# hello = 'hello'
# print(hello)
# print(hello[2:])


'''
Python List
'''
ls = ['abcd', 786, 2.23, 'john', 78.2]
tinylist = [123, 'john']

#Read: ls의 목록을 출력
print(ls)

#Create:ls에 100을 추가
ls.append('100')
print(ls)

#Update: ls와 tinyls의 결합
print(ls+tinylist)

#Delete: ls에서 786을 제거
del ls[1]
print(ls)

# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')

# Create: tp 에 '100'을 추가 Create
# -> 튜플은 요소값을 더하거나 뺄 수 없다.

# Read: tp 의 목록을 출력
print(tp)

# Update: tp와 tinytp 의 결합
print(tp+tinytp)

# Delete: tp 에서 786을 제거
# 제거 불가~~~

print("<<Dictionary part>>")
# dictionary CRUD Example
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'name':'홍', 'age':'30세'}

# Create: dt 에 '100'을 추가 Create
dt['number'] = 100
print(f'create:{dt}')

# Read: dt 의 목록을 출력
dt.items()
print(f'print로 했을때 {dt}')

# Delete: dt 에서 'abcd' 제거
del dt['abcd']
dt.items()
print(f'del:{dt}')

# Update: dt와 tinydt 의 결합
print(dt.update(tinydt))
print(f'dt.update(tinydt):{dt}')
print(tinydt.update(dt))  # tinydt에  dt를 덮어썼을 때
print(f'tinydt.update(dt):{dt}')





