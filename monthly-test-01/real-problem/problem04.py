############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    sortedList = [] # 중복값이 삭제된 리스트
    pNum = 0 # 양수들의 합
    mNum = 0 # 음수들의 합 
    if items_list:
        for item in items_list: 
            # 만약 sortedlist에 itemlist의 요소가 없다면 추가하는 코드를 작성했다. 
            # 이 코드로 중복값은 추가가 되지 않는다.
            if item not in sortedList:
                sortedList.append(item)
        
    for num in sortedList:
        # num 이 정수인 경우에만 양수와 음수를 각각 합산하도록 코드를 작성했다.
        if isinstance(num, int):
            if num < 0:
                mNum += num
            else:
                pNum += num
        else:
            continue
    return sortedList, (pNum, mNum)



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_items([2, 2, 2, "a", "a", 3, 0, -2]))
# 예시 결과: ([2, "a", 3, 0, -2], (5, -2))

print(analyze_items([]))
# 예시 결과: ([], (0, 0))

print(analyze_items(["apple", "apple", "banana"]))
# 예시 결과: (["apple", "banana"], (0, 0))
#####################################################
