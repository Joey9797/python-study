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

apple = ['사과', 'apple']
banana = ['바나나', 'banana']
kiwi = ['키위', 'kiwi']

fruit_str = "는 영어로 "

print(f'''{apple[0] + fruit_str + apple[1]} 
{banana[0] + fruit_str + banana[1]}
{kiwi[0] + fruit_str + kiwi[1]}''')