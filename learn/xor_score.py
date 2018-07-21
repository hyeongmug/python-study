from sklearn import svm, metrics

clf = svm.SVC()

datas = [[0, 0], [1, 0], [0, 1], [1, 1]]
labels = [0, 1, 1, 0]
examples = [[0, 0], [1, 0]]
examples_label = [0, 1]

# clf.fit(데이터, 답(label))
clf.fit(datas, labels)

# clf.predict(얻고 싶은 데이터)
results = clf.predict(examples)
print(results)

# metrics.accuracy_score(진짜답, 예측한답)
score = metrics.accuracy_score(examples_label, results)
print("정답률:", score)
