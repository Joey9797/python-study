import requests
import pprint

# 하드 코딩하는 변수(즉 변하지 않는 값 "상수")는 변수명 대문자로 작성
URL = 'https://fakestoreapi.com/carts' # 요청 주소

#.get() : 요청을 보내는 메서드
data = requests.get(URL)
print(data)
# 출력 결과 : <Response [200]>
# [200] : 웹의 응답 코드 -> 정상적으로 응답하였습니다.
# [404] : 웹의 응답 코드 -> 요청이 잘못되었습니다. (알 수 없는 주소로 요청했다)

# .json() : 데이터를 JSON 형태로 변환해주는 메서드
json_data = data.json()
print(type(json_data)) # 타입은 리스트(딕셔너리로 이루어진)
pprint.pprint(json_data) # 이쁘게 출력하자

