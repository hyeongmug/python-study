# dictionary 관련 함수들

# Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
b = a.keys()  # a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys라는 객체를 리턴한다.
print(b)

for k in a.keys():  # dict_keys객체도 list처럼 for문을 사용할수 있다.
    print(k)

# dict_keys 객체를 리스트로 변환
l = list(a.keys())
print(l)

# Value 리스트 만들기(values)
c = a.values()
print(c)

# Key, Value 쌍 얻기(items)
d = a.items()
print(d)

# Key:Value 쌍 모두 지우기(clear)
a.clear()
print(a)

# key로 value얻기(get)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('nokey'))
# print(a['nokey'])
"""
a.get('name')은 a['name']을 사용했을 때와 동일한 결과
차이점은 a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고 할 경우 
a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을 리턴
"""

# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print( 'name' in a, 'email' in a )
