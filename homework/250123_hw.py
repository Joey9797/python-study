# # ------------------------------------------
# #  ws_4_2
# list_of_book = [
#     '장화홍련전',
#     '가락국 신화',
#     '온달 설화',
#     '금오신화',
#     '이생규장전',
#     '만복자서포기',
#     '수성지',
#     '백호집',
#     '원생몽유록',
#     '홍길동전',
#     '장생전',
#     '도문대작',
#     '옥루몽',
#     '옥련몽',
# ]


# rental_list = [
#     '장생전',
#     '원생몽유록',
#     '이생규장전',
#     '장화홍련전',
#     '수성지',
#     '백호집',
#     '난중일기',
#     '홍길동전',
#     '만복자서포기',
# ]

# bookList = []

# for book in rental_list:
#     if book in list_of_book:
#        bookList.append(book)
#     else :
#         print(f'{book}은 보유하고있지 않습니다')
#         break
    
# if all(book in list_of_book for book in bookList ):
#     print('모든 도서가 대여 가능한 상태입니다.')




# # ------------------------------------------
# #  ws_4_4
# list_of_book = [
#     '장화홍련전',
#     '가락국 신화',
#     '온달 설화',
#     '금오신화',
#     '이생규장전',
#     '만복자서포기',
#     '수성지',
#     '백호집',
#     '원생몽유록',
#     '홍길동전',
#     '장생전',
#     '도문대작',
#     '옥루몽',
#     '옥련몽',
# ]

# rental_list = [
#     '장생전',
#     '위대한 개츠비',
#     '원생몽유록',
#     '이생규장전',
#     '데미안',
#     '장화홍련전',
#     '수성지',
#     '백호집',
#     '난중일기',
#     '홍길동전',
#     '만복자서포기',
# ]

# canRentalBook = [book for book in rental_list
#                  if book in list_of_book]

# missingBook = [book for book in rental_list 
#                if book not in list_of_book]

# if missingBook:
#     for book in missingBook:
#         print(f'{book}을/를 보충하여야 합니다.')
# elif all(book in list_of_book for book in canRentalBook):
#     print('모든 도서가 대여 가능한 상태입니다.')

    


# # ------------------------------------------
# #  ws_4_b
# food_list = [
#     {
#         '종류': '한식',
#         '이름': '잡채'
#     },
#     {
#         '종류': '채소',
#         '이름': '토마토'
#     },
#     {
#         '종류': '중식',
#         '이름': '자장면'
#     },
# ]

# for food in food_list:
#     print(f"{food['이름']}은/는 {food['종류']}(이)다.")
#     if food['이름'] == '토마토':
#         food['종류'] = '과일'
#     elif food['이름'] == '자장면':
#         print('자장면엔 고춧가루지')
        
# print(food_list)




# # ------------------------------------------
# #  ws_4_c

# matrix = [
#         ['0, 1', '0, 2', '0, 3'], 
#         ['1, 0', '1, 1', '1, 2', '1, 3'], 
#         ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
#         ['3, 0', '3, 1'], 
#         ['4, 0', '4, 1', '4, 2'], 
#         ['5, 0']
#     ]

# matrixLen = 0
# for len in matrix:
#        matrixLen += 1
       
# print(matrixLen)


# for list in matrix:
#     temporaryLen = 0
#     for number in list:
#         temporaryLen += 1
#     if temporaryLen <= 4:
#         print(f"'{list}' 리스트는 {temporaryLen}개 만큼 요소를 가지고 있습니다.")
        
# for i, list in enumerate(matrix):
#     for j, number in enumerate(list):
#         print(f"matrix의 {i},{j}번째 요소의 값은 {matrix[i][j]}입니다.")
        



# # ------------------------------------------
# #  ws_4_1
# import requests
# from pprint import pprint as print

# # 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])

# companyName = parsed_data['company']['name']
# print(companyName)




# # ------------------------------------------
# #  ws_4_2
# import requests
# from pprint import pprint as print

# dummy_data = []

# for i in range(1, 11):
#     API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
#     response = requests.get(API_URL)
#     parsed_data = response.json()
#     dummy_data.append(parsed_data['name'])
    
# print(dummy_data)




# # ------------------------------------------
# #  ws_4_3
import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    companyName = parsed_data['company']['name']
    lat = parsed_data['address']['geo']['lat']
    lng = parsed_data['address']['geo']['lng']
    
    if (-80 < float(lat) < 80 and -80 < float(lng) < 80):
         dummy_data.append({'name':parsed_data['name'], 'lat':lat, 'lng':lng, 'company name':companyName})
    else:
        dummy_data.append({'name':parsed_data['name'], 'company name':companyName})
    
print(dummy_data)




# # ------------------------------------------
# #  ws_4_4