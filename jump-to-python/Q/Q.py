A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# i = 0
# result = 0
# while i < len(A) :
#     if A[i] >= 50 :
#         result += A[i]
#     i += 1
# print(result)


result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark
print(result)