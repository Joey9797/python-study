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


    


