# 파일 객체 = open(파일 이름, 파일 열기 모드)
f = open("newfile.txt", 'w')
f.close()

# r	읽기모드 - 파일을 읽기만 할 때 사용
# w	쓰기모드 - 파일에 내용을 쓸 때 사용
# a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용


# 파일을 쓰기 모드로 열어 출력값 적기
f = open("D:/02.Python/새파일.txt", 'w', encoding='utf-8')
for i in range(1, 11):
    data = "%d 번째 줄입니다. \n" % i
    f.write(data)
f.close()


# with
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
# with문을 이용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close됨
