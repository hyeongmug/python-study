from sklearn import svm

clf = svm.SVC()
# clf.fit(데이터, 답(label))
clf.fit([
    [0, 0], # 배열에서 각각인 부분들을 벡터라고 부른다.
    [1, 0],
    [0, 1],
    [1, 1],
], [
    0,
    1,
    1,
    0
])
results = clf.predict([  # 답을 얻고싶은 데이터를 넣음
    [0, 0],
    [1, 0]
])
print(results)