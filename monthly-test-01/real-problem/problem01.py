############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):
    sumData = 0  # sumData는 좋아요의 합계를 담기 위한 변수
    for num in weekly_like_list:
        sumData += num # 좋아요수 리스트를 순회하며 나온 숫자를 sumData에 계속 더해간다.
    avData = sumData / 7 # sumData(좋아요의 총합)을 7로 나눈 평균을 avData 변수에 담는다.
    
    #minBaseData 는 좋아요 수의 최솟값을 구하기 위한 기준값(index 0번째 값)이다.
    minBaseData = weekly_like_list[0] 
    for num in weekly_like_list: 
         # 만약 들어온 숫자가 기준값(minBaseData)보다 작으면 기준값을을 업데이트한다.
         # 최종적으로 가장 최솟값이 minBaseData에 들어가게 된다.
        if num < minBaseData:
            minBaseData = num
    
    #아래 부분은 최댓값을 구하는 부분이다. minBaseData와 같은 방식으로 동작한다. 
    maxBaseData = weekly_like_list[0]
    for num in weekly_like_list:
        if num > maxBaseData:
            maxBaseData = num

    #아래 영역은 최댓값 - 최솟값을 구하는 부분이다.
    finalData = 0
    if minBaseData == maxBaseData: # 최솟값과 최댓값이 같다면(모든 수의 값이 같다면)
        finalData = 0 # 0을 finalData에 담고
    else:
        finalData = maxBaseData - minBaseData # 그렇지 않다면 최댓값에서 최솟값을 뺸 값을 finalData에 담는다.
    
    return avData, finalData # 최종적으로 좋아요수의 평균값과 최댓값-최솟값 을 반환한다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
analyze_likes([2, 5, 3, 8, 0, 10, 4])
# 1) 평균 = (2 + 5 + 3 + 8 + 0 + 10 + 4) / 7
#    = 32 / 7 ≈ 4.5714...
# 2) 최소=0, 최대=10, 차이=10
# 결과: (4.5714..., 10)
print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)

#####################################################
