'''
문제 4: 대문자 포함 여부 확인

문자열에 대문자가 포함되어 있는지 확인하는 함수를 작성하시오.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def contains_uppercase(string):
    for alpha in string:
        if alpha.isupper():
            return True
    return False

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(contains_uppercase('helLo'))  # True
print(contains_uppercase('world'))  # False
#####################################################