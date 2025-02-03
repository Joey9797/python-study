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



# import random

# celsius_temps = [0, 10, 15, 20, 25, 30, 35]
# random.shuffle(celsius_temps)
# print(celsius_temps)

# result = list(map(lambda x :"HOT" if  x >= 16.5 else "COLD", celsius_temps))
# print(result)

# def decideTemp(a):
#     if a >= 16.5:
#         return 'HOT'
    
#     else:
#         return 'COLD'
    
# result = list(map(decideTemp, celsius_temps))
# print(result)

# my_dict = {'a': 10, 'b': 5, 'c': 15}

# min_key = min(my_dict, key=lambda x : my_dict[x])
# print(min_key)

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newList = [myList.pop() 
#            for num in myList]
# print(newList)

# num = [1, 2, 3, 4, 5]
# newList = list(map(lambda x: "짝수" if num % 2 = 0 else "홀수", [1, 2, 3, 4, 5]))



# #--------------------------------------------
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [2, 3, 4, 5, 6]

# # 짝수면 "짝수", 홀수면 "홀수"로 변환
# result = list(map(lambda x: "짝수" if x[0] % 2 == 0 and x[1] % 2 == 0 else "홀수", zip(numbers1, numbers2)))
# print(result) # ['홀수', '홀수', '홀수', '홀수', '홀수']

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = set2 - set1
# print(set3)




# # --------------------------------------------
# # 10진수 2진수로 만들고, 2진수는 str으로 만들기
# def dec_to_bin(num):  
#     binary = []
#     number = num
#     while number > 0:
#         if number % 2 == 0:
#             binary.append(number % 2)
#             number //= 2
#         else:
#             binary.append(number % 2)
#             number //= 2
#     return binary[::-1]
#     # binary.reverse()
#     # return binary

# print(dec_to_bin(10))

# print(bin(10))





# #  --------------------------------------------
# #  평균값을 계산하는 함수 average
# def average(lst):
#     return sum(lst) / len(lst)
    
# print(average([3, 6, 5, 7]))





#  --------------------------------------------
#  최대값 최솟값 계산하는 함수 max_max
def max_max(lst):
    num = lst[0]
    for num in lst:
        if num <= lst[0]:
            num = num
        else:
            num = lst[0]
    return num

print(max_max([1, 2, 0, 5, 0, 0, -1]))






#  --------------------------------------------
#  딕셔너리 내의 특정 값 조건문으로 확인 is_rate
def 

    


