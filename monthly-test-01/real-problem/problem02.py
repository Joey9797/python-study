############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

# def analyze_treasures(treasure_list, threshold):
#     keyList = []
#     for treasure in treasure_list:
#         if treasure not in keyList:
#             keyList.append(treasure)

def analyze_treasures(treasure_list, threshold):
    sortedList = sorted(treasure_list)
    totalGroup = []
    group = [sortedList[0]]
    for i in range(1, len(sortedList)):
        if sortedList[i] == sortedList[i - 1]:
            group.append(sortedList[i])
        else:
            totalGroup.append(group)
            group = [sortedList[i]]
    totalGroup.append(group)
        
    return totalGroup, threshold


(['coin', 'coin', 'diamond', 'gold', 'gold', 'gold', 'silver'], 1)

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))S

#####################################################
# 아래 테스트 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_treasures(["gold", "silver", "gold", "gold", "diamond", "coin", "coin"], 1))
# ({'gold': 2, 'silver': 1, 'diamond': 1, 'coin': 2}, 2)

# print(analyze_treasures([], 3))
# # ({}, 0)

# print(analyze_treasures(["pearl", "pearl", "ruby"], 2))
# # ({'pearl': 2, 'ruby': 1}, 0)
#####################################################
