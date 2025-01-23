# 1부터 16까지의 숫자를 4x4로 변환
# one_d_list = list(range(1, 17))
# matrix = [one_d_list[i:i+4] for i in range(0, len(one_d_list), 4)]
# print(matrix)

# happy = 'happy'
# print(happy)
# print(type(happy))

# bugs = 'roaches'
# counts = '13'
# area = 'living room'

# print(f'Debugging {3+5} {bugs} {counts}')

# # 문자열의 시퀀스 특징
# my_str = 'hello world'
# # 1. 인덱싱
# print(my_str[1])  # e

# # 2. 슬라이싱
# print(my_str[2:4])  # ll
# print(my_str[:2])  # hel
# print(my_str[3:])  # lo
# print(my_str[::5])  # hlo
# print(my_str[::-1])  # olleh
# print(my_str[:])

# 사과는 영어로 apple
# 바나나는 영어로 banana
# 키위는 영어로 kiwi

# apple = ['사과', 'apple']
# banana = ['바나나', 'banana']
# kiwi = ['키위', 'kiwi']

# fruit_str = "는 영어로 "

# print(f'''{apple[0] + fruit_str + apple[1]} 
# {banana[0] + fruit_str + banana[1]}
# {kiwi[0] + fruit_str + kiwi[1]}''')

# #------------------------------------
# # deepcopy
# import copy

# original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = copy.deepcopy(original)

# # 원본 값 변경
# original[0][0] = 99

# print(original)         
# print(new_list)   

# list1 = [1, 2, 3, 4, [5, 50]]
# list2 = list1.copy()
# list2[0] = 10
# list2.append(6)
# list2[4] = [100]

# print(list1)
# print(list2)

# a = 1
# b = 2

# def enclosed():
#     a = 10
#     c = 3

#     def local(c):
#         print(a, b, c)
    
#     local(300)
#     print(a, b, c)


# enclosed()
# print(a, b)

# numbers = ['1','2','3','4','5']
# numbers1 = list(map(int, numbers))
# print(numbers1)

# def greet(name, age=30):
#     print(f'안녕하세요, {name}님! {age}살이시군요!')

# greet(10, name='dave')



# def add_numbers(a, b):
#     sum = a+b
#     print(sum)

# add_numbers(3,8)



import random

celsius_temps = [0, 10, 15, 20, 25, 30, 35]
random.shuffle(celsius_temps)
print(celsius_temps)

result = list(map(lambda x :"HOT" if  x >= 16.5 else "COLD", celsius_temps))
print(result)

def decideTemp(a):
    if a >= 16.5:
        return 'HOT'
    
    else:
        return 'COLD'
    
result = list(map(decideTemp, celsius_temps))
print(result)
