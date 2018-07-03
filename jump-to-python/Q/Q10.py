vowels = 'aeiou'
sentence = 'Life is too short, you need python'
c = [a for a in sentence if a not in vowels]
a = ''.join(c)
print(c)
print(a)