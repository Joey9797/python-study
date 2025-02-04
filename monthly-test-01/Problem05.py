'''
문제 5: 최댓값 찾기 (내장 함수 금지)

정수로 이루어진 튜플이 주어질 때, 이 튜플에서 가장 큰 수를 반환하는 함수를 작성하시오.
'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def find_max_in_tuple(numbers):
    baseNum = numbers[0] 
    for num in numbers: 
        if num >= baseNum: 
            baseNum = num 
    return baseNum

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_in_tuple((1, 5, 3, 9, 2)))      # 9
print(find_max_in_tuple((-10, -20, -3, -5)))   # -3
print(find_max_in_tuple((100, 100, 99, 98)))   # 100
print(find_max_in_tuple((0, 0, 0, 0)))         # 0
print(find_max_in_tuple((42,)))                # 42
#####################################################