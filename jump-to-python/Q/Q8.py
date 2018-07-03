# arr = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# a = 0
# b = 0
# o = 0
# ab = 0

# for val in arr:
#     if val == 'A':
#         a += 1
#     if val == 'B':
#         b += 1
#     if val == 'O':
#         o += 1
#     if val == 'AB':
#         ab += 1

# print("A: %d" % a)
# print("B: %d" % b)
# print("O: %d" % o)
# print("AB: %d" % ab)


data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result = {}
for blood_type in data:
    if blood_type in result:
        result[blood_type] += 1
    else :
        result[blood_type] = 1

print(result)