# 딕셔너리 표현
my_dict_1 = {}
my_dict_2 = {'key':'value'}
my_dict_3 = {1:'apple', 'list':[1, 2, 3]}
print(my_dict_1)  # 
print(my_dict_2)  # 
print(my_dict_3)  # 


# 딕셔너리는 키에 접근해 값을 얻어냄
my_dict = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict['apple'])
print(my_dict['list'])


# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경

print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}
my_dict['apple'] = 100
print(my_dict['list'][1])