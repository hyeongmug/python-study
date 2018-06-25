str1 = "테스트 {} 입니다.".format("1")
print(str1)
str2 = "테스트{1}-{0} 입니다.".format(1,"2")
print(str2)
print("number test = {number:0.4f}".format(number=3.42134234))

name = 'david'
age = 30
print(f'my name is {name}, and {age} old year')
print(f'{"hi":=^10}')
print(f'{3.42134234:!<10.4f}')