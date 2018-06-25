# 1. 문자열 출력
print("\"jump to python\" questions")

# 2. 문자열 출력 2
a =  """
Life is too short
You need python
"""
print(a)

# 3. 공백 추가
print(' ' * 24 + "PYTHON")

# 4. 문자열 나누기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 5. 문자열 인덱싱
pin = "881120-1068234"
print(pin[7])

# 6. 문자열 변경
a = "1980M1120"
print( a[4]+a[:4]+a[5:] )

# 7. 문자열 포맷
print( "%30s" % "PYTHON" )

# 8. 문자열 찾기
a = "Life is too short, you need python"
print( a.find("short") )

# 9. 문자열 바꾸기1
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# 10. 문자열 바꾸기2
a = "a:b:c:d"
b = a.split(":")
print(b)
c = "#".join(b)
print(c)



