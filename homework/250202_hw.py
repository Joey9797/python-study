# # ------------------------------------------
# # ws_6_b
# data = {
#     '이름': '키위',
#     '종류': '새',
#     '원산지': '호주' 
# }

# plus_data = {
#     '종류': '과일',
#     '가격': 30000
# }
# # 1. data가 가진 모든 키와 벨류 목록을 출력한다.
# print(data.items())

# # 2. data가 가진 벨류 목록들만 모아서 출력한다.
# print(data.values())

# # 3. data에서 'without' 키가 가진 value를 출력한다.
#     # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
# print(data.get('without', 'unknown'))

# # 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
# data.update(plus_data)

# # 5. 변경된 data를 출력한다.
# print(data)






# # ------------------------------------------
# # ws_6_c
# def newData(data, keyList):
#     for dict in data:
#         print('\n')
#         for key in keyList:
#             dict.setdefault(key, 'unknown')
#             print(f'{key}은/는 {dict.get(key)}입니다.')
    

# data = [
#     {
#         'name': 'galxy flip',
#         'company': 'samsung',
#         'is_collapsible': True,
#     },
#     {
#         'name': 'ipad',
#         'is_collapsible': False
#     },
#     {
#         'name': 'galxy fold',
#         'company': 'samsung',
#         'is_collapsible': True
#     },
#     {
#         'name': 'galxy note',
#         'company': 'samsung',
#         'is_collapsible': False
#     },
#     {
#         'name': 'optimus',
#         'is_collapsible': False
#     },
# ]

# key_list = ['name', 'company', 'is_collapsible']

# newData(data, key_list)






# # ------------------------------------------
# # ws_6_2
# def get_value_from_dict(my_dict, key):
#     return my_dict.pop(key, 'Unknown')
    


# my_dict = {'name': 'Alice', 'age': 25}
# result = get_value_from_dict(my_dict, 'name')
# print(result)  # Alice

# result = get_value_from_dict(my_dict, 'gender')
# print(result)  # Unknown

person = {'name': 'Alice', 'age': 40}
print(person.setdefault('happy', 50))
print(person)






# # ------------------------------------------
# # ws_7_b
# class Myth:
#     type_of_myth = 0
    
#     def __init__(self, name):
#         self.name = name
#         Myth.num_type_of_myth()
        
#     @classmethod
#     def num_type_of_myth(cls):
#         cls.type_of_myth += 1
        
#     @staticmethod
#     def description():
#         print('신화는 한 나라 혹은 어쩌구저쩌구이다.')
        
# myth1 = Myth('dangun')
# myth2 = Myth('greek & rome')
# print(myth1.name)
# print(myth2.name)
# print(Myth.type_of_myth)
# Myth.description()





# # ------------------------------------------
# # ws_7_c
# class Car:
#     wheels = 4
    
#     def __init__(self, engine, driving_system, sound):
#         self.engine = engine
#         self.driving_system = driving_system
#         self.sound = sound
        
#     def drive(self):
#         print(self.sound)
#         return(self.engine)
    
#     def introduce(self):
#         print(f'제 차의 엔진은 {self.engine} 방식이고, {self.driving_system}(으)로 작동합니다.')
    
#     @classmethod
#     def increase_wheels(cls):
#         cls.wheels += 1
#         print('법이 개정되어 모든 자동차의 필요 바퀴 수가 1 증가하였습니다.')
        
#     @staticmethod
#     def descrpition():
#         print('자동차는 어쩌구저쩌구')

# car1 = Car('gasoline', '후륜구동', '부릉부릉')
# car2 = Car('diesel', '전륜구동', '달달달달')
# car3 = Car('hybrid', '4wd', '슈웅')

# car1.drive()
# print(car2.drive())

# print('===')
# car1.introduce()
# car3.introduce()

# print('===')
# print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
# Car.increase_wheels()
# print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
# Car.descrpition()






# # ------------------------------------------
# # ws_7_2
# 아래 클래스를 수정하시오.
# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
        
#     def calculate_area(self):
#         return self.width * self.height


# shape1 = Shape(5, 3)
# area1 = shape1.calculate_area()
# print(area1)