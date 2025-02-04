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
# def min_min(lst):
#     baseNum = lst[0]
#     for num in lst:
#         if num < baseNum:
#             baseNum = num
#     return baseNum

# print(min_min([1, 2, 0, 5, -1, 0, 5]))






'''
문제 2: 특정 값 확인 (is_rate)

딕셔너리 내에서 특정 키의 값이 10 이상인지 확인하는 함수를 작성하시오.
'''

def is_rate(data, key):
    pass

print(is_rate({"rate": 12, "score": 8}, "rate"))  # True
print(is_rate({"rate": 9, "score": 15}, "rate"))  # False
print(is_rate({"score": 20, "value": 5}, "rate"))  # False




'''
문제 3: 문자열 길이 반환 (my_length)

딕셔너리 내에서 특정 키의 값이 문자열일 경우, 그 길이를 반환하는 함수를 작성하시오.  
만약 해당 키가 없거나 값이 문자열이 아니면 0을 반환합니다.
'''

def my_length(data, key):
    pass

print(my_length({"name": "hello", "age": 25}, "name"))  # 5
print(my_length({"title": "Python", "views": 100}, "title"))  # 6
print(my_length({"content": 12345, "author": "Alice"}, "content"))  # 0
print(my_length({"score": 95, "level": "high"}, "rank"))  # 0




'''
문제 4: 딕셔너리 값의 합산 (sum_total)

딕셔너리 내의 모든 값이 숫자일 경우, 그 총합을 반환하는 함수를 작성하시오.  
만약 값 중 숫자가 아닌 것이 있으면, 숫자인 값들만 합산합니다.
'''

def sum_total(data):
    pass  # 함수 구현하기

print(sum_total({"a": 10, "b": 20, "c": 30}))  # 60
print(sum_total({"x": 5, "y": "hello", "z": 15}))  # 20
print(sum_total({"p": 3.5, "q": 7.5, "r": 2}))  # 13.0
print(sum_total({"m": "text", "n": "data"}))  # 0




'''
문제 5: 19살 이상 인원 카운트 (over_19)

사전 형태의 인원 정보가 담긴 리스트를 순회하여, 19살 이상인 인원의 수를 반환하는 함수를 작성하시오.  
각 인원 정보는 'age' 키를 가지고 있으며, 값이 19 이상이면 카운트합니다.
'''

def over_19(people):
    pass  # 함수 구현하기

print(over_19([{"name": "Alice", "age": 20}, {"name": "Bob", "age": 18}, {"name": "Charlie", "age": 22}]))  # 2
print(over_19([{"name": "David", "age": 17}, {"name": "Eve", "age": 16}]))  # 0
print(over_19([{"name": "Frank", "age": 19}, {"name": "Grace", "age": 21}, {"name": "Helen", "age": 19}]))  # 3
print(over_19([]))  # 0




'''
문제 6: 조건을 만족하는 합 계산 (calc)

가변인자로 전달된 숫자들 중 특정 조건을 만족하는 값들만 합산하여 반환하는 함수를 작성하시오.  
조건: 짝수인 경우 2로 나눈 값을 합산, 홀수인 경우 그대로 합산합니다.
'''

def calc(*numbers):
    pass  # 함수 구현하기

print(calc(1, 2, 3, 4, 5))  # 1 + (2/2) + 3 + (4/2) + 5 = 10
print(calc(10, 15, 20, 25))  # (10/2) + 15 + (20/2) + 25 = 50
print(calc(7, 14, 21, 28))  # 7 + (14/2) + 21 + (28/2) = 49
print(calc())  # 0




'''
문제 7: 카이사르 암호화 (caesar)

카이사르 암호는 문자의 아스키 코드 값을 기반으로 변형하는 간단한 치환 암호입니다.  
각 문자의 아스키 코드 값을 얻은 후, n 만큼 증가시킨 새로운 문자로 변환하여 암호화합니다.  
단, 공백은 변형하지 않습니다.

예시:
'A'의 아스키 코드 값은 65입니다.  
'A'를 n=3 만큼 이동시키면, 65 + 3 = 68 → 'D'가 됩니다.
'''

def caesar(text, n):
    pass  # 함수 구현하기

print(caesar("hello", 3))  # "khoor"
print(caesar("abc xyz", 2))  # "cde zab"
print(caesar("Python", 5))  # "Udymts"
print(caesar("Caesar Cipher", 1))  # "Dbftbs Djqifs"




'''
문제 8: 요소들의 곱 합산 (calc_product_price)

리스트 내에 있는 딕셔너리 요소들의 특정 키 값을 곱한 후, 그 결과들을 모두 합산하여 반환하는 함수를 작성하시오.  
각 딕셔너리는 'price'와 'quantity' 키를 가지며, 두 값을 곱한 후 총합을 계산합니다.
'''

def calc_product_price(items):
    pass  # 함수 구현하기

print(calc_product_price([
    {"price": 100, "quantity": 2},
    {"price": 200, "quantity": 1},
    {"price": 50, "quantity": 4}
]))  # 100*2 + 200*1 + 50*4 = 500

print(calc_product_price([
    {"price": 300, "quantity": 3},
    {"price": 150, "quantity": 2}
]))  # 300*3 + 150*2 = 1200

print(calc_product_price([]))  # 0

print(calc_product_price([
    {"price": 500, "quantity": 1},
    {"price": 1000, "quantity": 2},
    {"price": 200, "quantity": 0}
]))  # 500*1 + 1000*2 + 200*0 = 2500




'''
문제 9: 정수 리스트를 이용한 문자열 생성 (make_answer)

주어진 문자열에서 정수 리스트를 추출한 후, 해당 정수 값만큼 반복하여 새로운 문자열을 생성하는 함수를 작성하시오.  
정수는 공백으로 구분되어 있으며, 각 정수만큼 '*' 문자를 반복하여 결과를 만듭니다.

예시:
입력 문자열이 "3 5 2" 라면, 결과는 "*** ***** **"가 됩니다.
'''

def make_answer(text):
    pass  # 함수 구현하기

print(make_answer("3 5 2"))  # "*** ***** **"
print(make_answer("1 4 3"))  # "* **** ***"
print(make_answer("0 2 6"))  # "  ** ******"
print(make_answer(""))  # ""




'''
문제 10: 딕셔너리를 이용한 숫자 코드 변환 (change_pwd)

주어진 문자열을 딕셔너리를 사용하여 숫자로 변환하는 함수를 작성하시오.  
각 문자는 미리 정의된 딕셔너리의 키로 존재하며, 해당 값으로 치환됩니다.  
딕셔너리에 없는 문자는 그대로 유지됩니다.

예시:
변환 딕셔너리가 {"a": "1", "b": "2", "c": "3"}일 때,  
입력 문자열 "abc xyz"는 "123 xyz"로 변환됩니다.
'''

def change_pwd(text, mapping):
    pass  # 함수 구현하기

print(change_pwd("abc xyz", {"a": "1", "b": "2", "c": "3"}))  # "123 xyz"
print(change_pwd("hello", {"h": "4", "e": "3", "l": "1", "o": "0"}))  # "43110"
print(change_pwd("password", {"p": "9", "a": "8", "s": "5", "w": "3", "o": "0", "r": "7", "d": "2"}))  # "98553 072"
print(change_pwd("unchanged", {"x": "9", "y": "8", "z": "7"}))  # "unchanged"




'''
문제 11: 요소의 길이 계산 (my_count)

주어진 요소의 길이를 반환하는 함수를 작성하시오.  
입력값이 문자열, 리스트, 튜플, 딕셔너리인 경우 해당 길이를 반환하며,  
그 외의 타입(숫자 등)은 길이를 계산할 수 없으므로 0을 반환합니다.

예시:
입력값이 "hello"이면 결과는 5입니다.  
입력값이 [1, 2, 3, 4]이면 결과는 4입니다.
'''

def my_count(element):
    pass  # 함수 구현하기

print(my_count("hello"))  # 5
print(my_count([1, 2, 3, 4]))  # 4
print(my_count((10, 20, 30)))  # 3
print(my_count({"a": 1, "b": 2}))  # 2
print(my_count(100))  # 0




'''
문제 12: 소수 판별 (is_primes)

주어진 정수가 소수인지 판별하는 함수를 작성하시오.  
소수란 1과 자기 자신만을 약수로 가지는 1보다 큰 자연수입니다.

예시:
입력값이 7이면 결과는 True입니다.  
입력값이 10이면 결과는 False입니다.
'''

def is_primes(n):
    pass  # 함수 구현하기

print(is_primes(7))  # True
print(is_primes(10))  # False
print(is_primes(2))  # True
print(is_primes(1))  # False
print(is_primes(19))  # True




'''
문제 13: 문자열 내 숫자 합산 (calc_sum_number)

주어진 문자열에서 숫자만 추출하여 합산하는 함수를 작성하시오.  
문자열 내에 포함된 모든 숫자를 찾아 그 합을 반환합니다.

예시:
입력값이 "a1b2c3"이면 결과는 6입니다.  
입력값이 "hello123world"이면 결과는 123입니다.
'''

def calc_sum_number(text):
    pass  # 함수 구현하기

print(calc_sum_number("a1b2c3"))  # 6
print(calc_sum_number("hello123world"))  # 123
print(calc_sum_number("abc"))  # 0
print(calc_sum_number("9 apples and 10 oranges"))  # 19
print(calc_sum_number("100 and 200"))  # 300




'''
문제 14: 재귀를 이용한 자릿수 합 (sum_digit)

주어진 정수의 각 자릿수를 더하는 연산을 재귀적으로 수행하는 함수를 작성하시오.  
결과가 한 자릿수가 될 때까지 연산을 반복합니다.

예시:
입력값이 987이면, 9 + 8 + 7 = 24 → 2 + 4 = 6이므로 결과는 6입니다.  
입력값이 12345이면, 1 + 2 + 3 + 4 + 5 = 15 → 1 + 5 = 6이므로 결과는 6입니다.
'''

def sum_digit(n):
    pass  # 함수 구현하기

print(sum_digit(987))  # 6
print(sum_digit(12345))  # 6
print(sum_digit(9))  # 9
print(sum_digit(9999))  # 9
print(sum_digit(100))  # 1




'''
문제 15: 딕셔너리 내 특정 값 확인 (check_value)

주어진 딕셔너리에서 특정 키의 값이 조건을 만족하는지 확인하는 함수를 작성하시오.  
조건: 값이 50 이상이면 True, 그렇지 않으면 False를 반환합니다.  
해당 키가 존재하지 않으면 False를 반환합니다.

예시:
입력값이 {"score": 75, "level": 3}에서 키 "score"를 확인하면 결과는 True입니다.  
입력값이 {"score": 30, "level": 5}에서 키 "score"를 확인하면 결과는 False입니다.
'''

def check_value(data, key):
    pass  # 함수 구현하기

print(check_value({"score": 75, "level": 3}, "score"))  # True
print(check_value({"score": 30, "level": 5}, "score"))  # False
print(check_value({"points": 100, "rank": 1}, "score"))  # False
print(check_value({"score": 50}, "score"))  # True
print(check_value({"value": 49}, "value"))  # False








    


