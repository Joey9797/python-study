my_list = [1, 'a', 3, 'b', 5]

# 슬라이싱
print(my_list[2:4])  # [3, 'b']
print(my_list[:3])  # [1, 'a', 3]
print(my_list[-2:])  # ['b', 5]
print(my_list[::2])  # [1, 3, 5]
print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

print(len(my_list))

# # 길이
# print(len(my_list))  # 5

# 중첩된 리스트 접근
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(len(my_list))  #
print(my_list[4][2])  # !!!
print(my_list[4][1][-1])  # w

# # 리스트는 가변
# my_list = [1, 2, 3]
# print(my_list)

