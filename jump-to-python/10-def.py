# 일반적인 함수
def sum(a, b):
    return a + b


print(sum(10, 5))


# 입력값이 없는 함수
def say():
    return 'Hi'


print(say())


# 결과 값이 없는 함수
def multiply(a, b):
    print("%d, %d의 곱은 %d입니다." % (a, b, a*b))


multiply(3, 4)


# 입력값도 결과값도 없는 함수
def say2():
    print('hi2')


say2()


# 매게 변수 지정하여 호출하기
def sum2(a, b):
    return a+b


print(sum2(b=7, a=3))  # 순서 상관 없어짐


# 여러 개의 입력값을 받는 함수
# 1
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


print(sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 2
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


print(
    sum_mul('sum', 1, 2, 3, 4, 5),
    sum_mul('mul', 1, 2, 3, 4, 5)
)


# 키워드 파라미터 kwargs(keyword arguments)
# 1
def func(**kwargs):
    print(kwargs)


func(a=1)

# 2


def func2(*args, **kwargs):
    print(args)  # 튜플
    print(kwargs)  # 딕셔너리


func2(1, 2, 3, name='foo', age=3)


# 함수의 결과값은 언제나 하나
def sum_and_mul(a, b):
    return a+b, a*b


sum5, mul5 = sum_and_mul(3, 4)

print(sum5, mul5)


# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("ㅎㅁ", 30)


# 함수 안에서 함수 밖의 변수를 변경하느 ㄴ방법
# 1) return 이용하기
a = 1


def vartest(a):
    a = a+1
    return a


a = vartest(a)
print(a)


# 2) global 명령어 이용하기 ☆☆☆
a2 = 1


def vartest2():
    global a2
    a2 = a2+1


vartest2()
print(a2)  # 첫번째 방법보다 안좋은 방법임



# lambda - 함수를 한줄로 간결하게 만들 때 사용
"""
    lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
"""

sum = lambda a, b: a+b
print( sum(3,4) )


# list 에서의 lambda
myList = [lambda a,b:a+b, lambda a,b:a*b]
print( myList )
print( 
    myList[0](3,4), 
    myList[1](3,4)
)