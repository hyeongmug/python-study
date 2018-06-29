# 리스트 유형
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트의 인덱싱
a = [1, 2, 3]
print(a[0])
print(a[0] + a[2])
print(a[-1])

# 이중 리스트
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0])

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b, c)

# 리스트 연산자
# 1) 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 2) 리스트 반복하기(*)
a = [1, 2, 3]
print(a * 3)

# 리스트의 수정, 변경과 삭제
# 1) 리스트에서 하나의 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

# 2) 리스트에서 연속된 범위의 값 수정하기
a[1:2]
a[1:2] = ['a', 'b', 'c']
print(a)

# 3) [] 사용해 리스트 요소 삭제하기
a[1:3] = []
print(a)

# 4) del 함수 사용해 리스트 요소 삭제하기
del a[1] # 다른 방법 a[0:1] = []
print(a)

# 리스트 관련 함수들
# 리스트에 요소 추가하기(append)
a = [1,2,3]
a.append(4)
a.append([5,6])
print(a)

# 리스트 정렬(sort)
a = [1,4,3,2]
a.sort()
print(a)

# 리스트 뒤집기(reverse)
a = ['a','c','b']
a.reverse()
print(a)

# 위치 반환(index)
a = [1,2,3]
print( a.index(3) )
print( a.index(1) )

# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0,4)
print(a)

# 리스트 요소 제거(remove)
a = [1,2,3,1,2,3]
a.remove(3)
print(a)
a.remove(3)
print(a)

# 리스트 요소 끄집에내기(pop)
# pop()은 리스트의 맨 마지막 요소를 돌려 주고 그 요소는 삭제
a = [1,2,3]
a.pop()
print(a)

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3]
a.pop(1)
print(a)

# 리스트 확장(extend)
a = [1,2,3]
a.extend([4,5])
print(a)
b = [6,7]
a.extend(b)
print(a)
