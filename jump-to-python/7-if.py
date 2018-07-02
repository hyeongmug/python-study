# 비교 연산자

"""

x < y
x > y 
x == y
x != y
x >= y
x <= y

and
or
not

x in s
x not in s

"""

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# and, or, not
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# x in s, x not in s
print(1 in [1, 2, 3])  # True
print(1 not in [1, 2, 3])  # False
print('a' in ('a', 'b', 'c'))  # True
print('j' not in 'python')  # True


# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# 주머니에 돈이 있다면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass # 아무것도 실행시키고 싶이 않을때 사용함
else:
    print("카드를 꺼네라")


# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 
# 돈도 없고 카드도 없으면 걸어 가라
pcket = ['paper', 'handphone']
card = 1
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")


# 조건부 표현식
score = 10
message = "success" if score >= 60 else "failure"
print(message)