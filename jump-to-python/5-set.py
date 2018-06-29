"""
집합(set)은 파이썬 2.3부터 지원되기 시작한 자료형으로, 
집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형이다.
"""

# 집합 자료형은 다음과 같이 set 키워드를 이용해 만들 수 있다.
s1 = set([1, 2, 3])
print(s1)
s2 = set("Hello")
print(s2)

"""
집합 자료형의 특징.
중복을 허용하지 않는다.
순서가 없다(Unordered).
"""

# 리스트 or 튜플로 변환
s1 = set([1, 2, 3])
l1 = list(s1)  # 리스트로 변환
print(l1)
t1 = tuple(s1)  # 튜플로 변환
print(t1)


# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 1) 교집합(&)
print(s1 & s2)  # s1.intersection(s2)

# 2) 합집합(|)
print(s1 | s2)  # s1.union(s2)

# 3) 차집합
print(s1 - s2)  # s1.difference(s2)
print(s2-s1)  # s2.difference(s1)

# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

# 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
