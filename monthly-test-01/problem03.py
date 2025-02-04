############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# def is_user_data_valid(user_data):
#     falseData = 0
#     for data in user_data:
#         if user_data[data] == '':
#             falseData += 1
#     if falseData > 0:
#         return False
#     else:
#         return True

def is_user_data_valid(user_data):
    for value in user_data.values():
        if value == '':
            return False
    return True



    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '',
}
print(is_user_data_valid(user_data2)) # True
#####################################################