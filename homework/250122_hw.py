# # hw_3_4
# # 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
# negative = -3
# print(abs(negative))


# # 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
# empty_list = []
# print(bool(empty_list))


# # 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))


# # 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
# unsorted_list = ['하', '교', '캅', '의', '지', '가']
# print(sorted(unsorted_list))

# print(list(range(1,11)))




# # ------------------------------------------
# # # ws_3_1
# number_of_people = 0

# def increase_user():
#     global number_of_people
#     number_of_people += 1

# increase_user()
# print(number_of_people)




# # ------------------------------------------
# # ws_3_2
# number_of_people = 0
# userList = []

# def increase_user():
#     global number_of_people
#     number_of_people += 1

# def create_user():

#     name = str(input("이름을 입력해주세요"))
#     age = int(input("나이를 입력해주세요"))
#     address = str(input("주소를 입력해주세요"))

#     increase_user()
#     print(f'현재 가입된 회원 수 : {number_of_people}')
#     print(f'{name}님, 환영합니다!')

#     userList.append({'name': name, 'age': age, 'address': address})


# create_user()
# create_user()
# print(userList)




# # ------------------------------------------
# # # ws_3_3
# number_of_book = 100

# def rentalBook():
#     userName = str(input("고객님의 이름을 입력해주세요."))
#     bookAmount = int(input("몇 권의 책을 빌리시겠습니까?"))
#     return userName, bookAmount

# def decreaseBook(userName, bookAmount):
#     global number_of_book
#     number_of_book -= bookAmount
#     print(f'{userName}님이 {bookAmount}권을 대여하였습니다.')
#     print(f'남은 책의 수 : {number_of_book}')

# userName, bookAmount = rentalBook()
# decreaseBook(userName, bookAmount)




# # # ------------------------------------------
# # # # ws_3_4
# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부'] 

# # userList = []

# # for i in range(5):
# #     userdict = dict(name=name[i], age=age[i], address=address[i])
# #     userList.append(userdict)

# # print(userList)

# userTuple = zip(name, age, address)
# userList = list(map(lambda x: {'name':x[0], 'age':x[1], 'address':x[2]} ,userTuple))

# print(userList)




# # ------------------------------------------
# # # ws_3_5
# number_of_book = 100

# 내 코드 -----------------------------------
# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부'] 

# userTuple = zip(name, age, address)
# manyUser = list(map(lambda x: {'name':x[0], 'age':x[1], 'address':x[2]} ,userTuple))


# def create_user(name, age, address):
#     print(f'{name}님, 환영합니다!')
#     manyUser.append({'name': name, 'age': age, 'address': address})

#     return name, age


# def rentalBook(name, age):
#     bookAmount = age // 10
#     return name, bookAmount

# def decreaseBook(name, bookAmount):
#     global number_of_book
#     number_of_book -= bookAmount
#     print(f'{name}님이 {bookAmount}권을 대여하였습니다.')
#     print(f'남은 책의 수 : {number_of_book}')


# name, age = create_user('김싸피', 66, '강남')
# name, bookAmount = rentalBook(name, age)
# decreaseBook(name, bookAmount)
# print(manyUser)


# 다른 사람 코드 -----------------------------------
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def createUser(name, age, address):
    userInfo = {}
    userInfo['name'] = name
    userInfo['age'] = age
    userInfo['address'] = address
    print(f'{name}님 환영합니다!')
    return userInfo

userList = list(map(createUser, name, age, address))
infoList = list(map(createUser, name, age))

def rentalBook(info):
    print(f"{info['name']}님이 {info['age'//10]}권을 대여했습니다.")
    

print(rentalBook(infoList))













# def create_user(x, y, z):
#     # print(f'{x}님 환영합니다!')
#     user_info = {}
#     user_info['name'] = x
#     user_info['age'] = y
#     user_info['address'] = z
#     return user_info

# many_user = list(map(create_user, name, age, address))
# print(many_user)
# number_of_book = 100

# def decrease_book(number):
#     global number_of_book
#     number_of_book -= number
#     print(f'남은 책의 수 : {number_of_book}')

# def rental_book(info):
#     decrease_book(info['age']//10)
#     print(f"{info['name']}님이 {info['age']//10}권의 책을 대여하였습니다.")

# new_list = list(map(lambda d : {'name': d['name'], 'age': d['age']}, many_user))

# list(map(rental_book , new_list))