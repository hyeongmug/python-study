numbers = input('?')
numbers = numbers.split(',')
result = 0
for number in numbers:
    result += int(number)
print(result)