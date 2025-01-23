# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3
sum_result = num1 + num2
print(sum_result)

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2

# 함수를 호출하여 결과 출력
sum_result = get_sum(num1, num2)
print(sum_result)


def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2


def nothing(a="nothing"):
    print('nothing :', a)

nothing()

# 함수와 반환 값
# print() 함수는 반환값이 없다.
