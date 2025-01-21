# 단축 평가

vowels = 'aeiou'

print(('a' and 'b') in vowels)  # false
print(('b' and 'a') in vowels)  # True
print(('b' or 'a') in vowels) # false
print(('a' or 'b') in vowels) # true

print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0
print(0 and 0)  # 0

print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0
