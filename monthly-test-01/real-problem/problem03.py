############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def find_most_populated(animal_map):
    if animal_map:
        # 람다를 이용하여 max값을 구하는 기준을 animal_map의 value값으로 설정했다.
        maxAnimal = max(animal_map, key=lambda x: animal_map[x])
        return maxAnimal
    else:
        return None # 만약 animal_map 이 비어있다면 None을 반환하도록 설정했다.
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(find_most_populated({"lion": 5, "tiger": 3, "elephant": 10}))  # 예시: "elephant"
print(find_most_populated({}))                                       # None
print(find_most_populated({"wolf": 4, "wolfdog": 4, "hyena": 4}))     # "wolf"
#####################################################
