# 메모리의 주소
a = [1, 2, 3]
print(id(a))


# 변수의 복사
a = [1, 2, 3]
b = a
print(id(a), id(b))  # 주소값 동일
print( a is b ) # True

a[1] = 4
print(a,b) # 동일


# 복사

# 1) [:] 이용
a = [1,2,3]
b = a[:]
a[1] = 4
print(a,b) # 다름

# 2) copy 모듈 이용 
from copy import copy # 깊은 복사시에는 from copy import deepcopy
a = [1,2,3]
b = copy(a)
print( b is a ) # False

# 변수를 만드는 여러 가지 방법
a, b = ('python','life')
print(a,b)

[a,b] = ['python', 'life']
print(a,b)

a = b = 'python'
print(a,b)
print(a is b) # True

# 두 변수의 값 바꾸기 ★★★
a = 3
b = 5
a, b = b, a
print(a, b)