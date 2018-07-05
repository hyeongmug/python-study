f1 = open("test.txt", 'w')
f1.write("Life is too shor!")
f1.close()


f2 = open("test.txt", 'r')
print(f2.read())
f2.close()



#  close를 명시적으로 할 필요가 없는 with구문
with open("test.txt", 'w') as f1:
    f1.write("Life is too short!")

with open("test.txt", 'r') as f2:
    print(f2.read())

    

# 'a' 모드
user_input = input("저장할 내용을 입력하세요:")
f = open('abc.txt', 'a')  # 내용을 추가하기 위해서 'a'를 사용
f.write(user_input)
f.write("\n")  # 입력된 내용을 줄단위로 구분하기 위해 줄바꿈 문자 삽입
f.close()


# 역순 저장
f = open('abc.txt', 'r')
lines = f.readlines() # 모든 라인을 읽음
f.close()

print(lines)

rlines = reversed(lines) # 읽은 라인을 역순으로 정렬

f = open('abc.txt', 'w')
for line in rlines:
    line = line.strip() # 포함되어 있는 줄바꿈 문자 제거
    f.write(line)
    f.write('\n') # 줄바꿈 문자 삽입
