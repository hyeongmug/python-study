# 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)



# 다양한 for문 ☆☆☆
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)



# for문의 응용
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격 입니다." % number)



# for문과 continue
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)



# for와 함께 자주 사용하는 range함수
a = range(10)  # 0부터 10미만의 숫자
print(a)

a = range(1, 11)  # range(시작 숫자, 끝 숫자)
print(a)



# range 예시

# 1
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

# 2
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')




# 리스트 안에 for문 포함하기(리스트 내포(List comprehension)) ☆☆☆ 

"""
[표현식 for 항목 in 반복 가능 객체 if 조건]
"""

# 1
result = [num * 3 for num in a]
print(result)

# 2
result = [num * 3 for num in a if num % 2 == 0]
print(result)


# for문을 여러개 사용할때의 리스트 내포

"""
[표현식 for 항목1 in 반복가능객체1 if 조건1
        for 항목2 in 반복가능객체2 if 조건2
        ···
        for 항몽n in 반복가능객체n if 조건n]
"""

# 구구단 예시
result = [x*y for x in range(2,10) 
              for y in range(1,10)]
print(result)

