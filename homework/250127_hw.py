# # ------------------------------------------
# # ws_4_4
# import requests
# from pprint import pprint as print

# black_list = [
#     'Hoeger LLC',
#     'Keebler LLC',
#     'Yost and Sons',
#     'Johns Group',
#     'Romaguera-Crona',
# ]

# censoredUserList = {}

# def create_user(company, userName):
#     if censorship(company, userName) is True:
#         censoredUserList[company] = [userName]
#         return censoredUserList


# def censorship(company, userName):
#     if company in black_list:
#         print(f'{company}소속의 {userName}은/는 등록할 수 없습니다.')
#         return False
#     else:
#         print(f'이상 없습니다.')
#         return True


# for i in range(1, 11):
#     API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
#     response = requests.get(API_URL)
#     parsed_data = response.json()
    
#     company = parsed_data['company']['name']
#     userName = parsed_data['name']

#     create_user(company, userName)

# print(censoredUserList)

'''
{'address': {'city': 'Gwenborough',
             'geo': {'lat': '-37.3159', 'lng': '81.1496'},
             'street': 'Kulas Light',
             'suite': 'Apt. 556',
             'zipcode': '92998-3874'},
 'company': {'bs': 'harness real-time e-markets',
             'catchPhrase': 'Multi-layered client-server neural-net',
             'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
'''

# # ------------------------------------------
# # ws_4_5
import copy
import pprint


user_data = [
    {
        'blood_group': 'AB',
        'company': 'Stone Inc',
        'mail': 'ian17yahoo.com',
        'name': 'Kathryn Jenkins',
        'website': [
            'https://www.boyd-herrera.com/',
            'https://watson.com/',
            'http://www.mitchell.com/',
            'http://irwin-cline.biz/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fleming Ltd',
        'mail': 'patricianelsonyahoo.com',
        'name': 'Angel Williamson',
        'website': [
            'https://wilson-johnson.com/',
            'https://santiago-hammond.com/',
            'https://morales.com/',
            'https://fry-fleming.com/',
        ],
    },
    {
        'blood_group': 'A+',
        'company': 'Scott PLC',
        'mail': 'lisajones@gmail.com',
        'name': 'Stephanie Herman MD',
        'website': [
            'https://www.boyer-stevens.org/',
            'http://www.johnson.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Warren-Stewart',
        'mail': 'allisonjennifer@gmail.com',
        'name': 'Jon Martinez',
        'website': ['https://www.berg.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fisher Inc',
        'mail': 'mross@yahoo.com',
        'name': 'Justin Brown',
        'website': [
            'https://www.gray.com/',
            'https://jones.com/',
            'http://williams.biz/',
            'https://hammond.net/',
        ],
    },
    {
        'blood_group': 'B-',
        'company': 'Pearson Group',
        'mail': 'gravesbarbara@hotmail.com',
        'name': 'Bobby Patterson',
        'website': ['https://www.cunningham.biz/', 'https://johnson.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'White, Andrade and Howard',
        'mail': 'mcole@gmail.com',
        'name': 'Michelle Strickland',
        'website': ['http://www.rose-gomez.com/', 'https://reilly.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Young',
        'mail': 'tmorales@hotmail.com',
        'name': 'Stephanie Moore',
        'website': ['https://schmidt.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Brooks PLC',
        'mail': 'wellsmatthew@hotmail.com',
        'name': 'Dr. David Johnson',
        'website': [
            'http://ford-dean.com/',
            'http://www.petersen.com/',
            'https://thompson-cooley.info/',
            'http://ryan-gay.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Stewart Group',
        'mail': 'sean37@hotmail.com',
        'name': 'Veronica Webb',
        'website': ['http://www.holmes.info/', 'http://www.morris.biz/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Cabrera, Perry and Harris',
        'mail': 'bgonzales@yahoo.com',
        'name': 'Lisa Wilcox',
        'website': ['https://www.small.com/', 'http://martin-petersen.com/'],
    },
    {
        'blood_group': 'B+',
        'company': 'Thomas, Lozano and Lopez',
        'mail': 'bperry@yahoo.com',
        'name': 'Brian Simmons',
        'website': [
            'http://reid.com/',
            'http://www.roman-neal.biz/',
            'https://www.hoover.org/',
            'https://www.lynn.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Baker-Leach',
        'mail': 'johnlucas@yahoo.com',
        'name': 'Carlos Robinson',
        'website': ['https://martin.com/', 'http://montgomery-cline.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Higgins, Higgins and Garcia',
        'mail': 'chris66@gmail.com',
        'name': 'Gabriel Collins',
        'website': ['https://www.cole-pugh.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Tanner, Wheeler and Weaver',
        'mail': 'leonardtammy@gmail.com',
        'name': 'Christopher Cook',
        'website': [
            'https://www.myers-reynolds.com/',
            'https://dunlap-rogers.com/',
            'https://luna.net/',
            'http://smith-miller.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Schaefer-Hunter',
        'mail': 'nsummers@gmail.com',
        'name': 'Daniel Monroe',
        'website': [
            'https://cook.net/',
            'http://carpenter.com/',
            'http://morris-terrell.com/',
        ],
    },
    {
        'blood_group': 'B+',
        'company': 'Stephens Group',
        'mail': 'rolson@gmail.com',
        'name': 'Molly Parks',
        'website': [
            'https://wright-vincent.biz/',
            'http://www.cruz.com/',
            'http://olson.org/',
            'http://gomez.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Fitzgerald, Costa and Hobbs',
        'mail': 'jennifervang@hotmail.com',
        'name': 'Jill Patterson',
        'website': [
            'https://www.brewer.com/',
            'https://malone-murray.info/',
            'http://evans.com/',
            'https://ortiz.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Frazier Ltd',
        'mail': 'vsolis@hotmail.com',
        'name': 'Marie May',
        'website': [
            'http://pratt.info/',
            'http://www.ortega.com/',
            'http://www.smith.net/',
            'https://nichols.biz/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Rodriguez and Sons',
        'mail': 'michael09@yahoo.com',
        'name': 'Julia Gonzalez',
        'website': [
            'https://www.cantrell.com/',
            'https://www.smith.net/',
            'http://delgado.com/',
            'http://stevens.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Arnold',
        'mail': 'christopher79@hotmail.com',
        'name': 'David Garza',
        'website': ['https://price.net/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Butler-Hernandez',
        'mail': 'angiechoi@yahoo.com',
        'name': 'Leslie Kemp',
        'website': ['http://www.martin-thompson.org/', 'http://martin.org/'],
    },
    {
        'blood_group': 'A-',
        'company': 'Schneider-Hensley',
        'mail': 'cesarsantos@hotmail.com',
        'name': 'Brandon Peterson',
        'website': [
            'https://www.owens-gay.com/',
            'https://www.santiago.org/',
            'https://www.singleton.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Hunter, Alvarado and Stewart',
        'mail': 'thomas16@gmail.com',
        'name': 'Matthew Stanley',
        'website': ['https://nelson.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Elliott, Mullins and Michael',
        'mail': 'smithedward@hotmail.com',
        'name': 'Robert Brown',
        'website': [
            'http://montgomery-rogers.biz/',
            'http://www.williams-nixon.com/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Velasquez-Garcia',
        'mail': 'samanthawilson@yahoo.com',
        'name': 'Stephanie Cohen',
        'website': ['http://jackson-harris.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Mccoy-Hopkins',
        'mail': 'lli@yahoo.com',
        'name': 'Michael Clark',
        'website': [
            'https://www.harding.info/',
            'https://www.jones.biz/',
            'http://knight-adkins.org/',
            'http://www.alvarado-mendoza.org/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Kerr Ltd',
        'mail': 'georgebrittany@yahoo.com',
        'name': 'Brandon White',
        'website': [
            'https://flowers-parker.info/',
            'http://oliver-rice.info/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Villarreal, Wood and Smith',
        'mail': 'denise73@yahoo.com',
        'name': 'Kevin Blevins',
        'website': [
            'http://www.ramirez.info/',
            'https://mckay.net/',
            'http://duran.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Jenkins-Garcia',
        'mail': 'kwoodward@hotmail.com',
        'name': 'Michelle Dixon',
        'website': [
            'http://www.taylor.com/',
            'https://bates-trujillo.org/',
            'https://www.thomas-boyer.org/',
        ],
    },
]

blood_types = ['A-', 'A+', 'B-', 'B+', 'O-', 'O+', 'AB-', 'AB+']
black_list = [
    'Jenkins-Garcia',
    'Stephens Group',
    'White, Andrade and Howard',
    'Warren-Stewart',
]

def createUser(lst):
    copyList = copy.deepcopy(lst)
    userList = []
    count = 0

    for user in copyList:
        result = isValidation(user)
        if result == True:
            userList.append(user)
        elif result[0] == False:
            count += 1
            for userKey in user:
                for resultKey in result[1]:
                    if resultKey == userKey:
                        user[userKey] = None
            user['* invalid'] = result[1]
            userList.append(user)
            

        elif result == 'blocked':
            count += 1

    print(f'잘못된 데이터로 구성된 유저의 수는 {count}입니다.')
    return userList
            
def isValidation(user):
    invalidList = []
    
    if user['company'] in black_list:
        return 'blocked'

    if user['blood_group'] not in blood_types:
        invalidList.append('blood_group')
    if '@' not in user['mail']:
        invalidList.append('mail')
    if len(user['website']) < 1:
        invalidList.append('website')
    if len(user['name']) < 2 or len(user['name']) > 30:
        invalidList.append('name')

    if not invalidList:
        return True
    elif invalidList:
        return False, invalidList

result = createUser(user_data)
print(len(result))
pprint.pprint(result)

# result = "\n\n".join(json.dumps(user, indent=4, ensure_ascii=False) for user in createUser(user_data))


# def makeResult(lst):
#     resultList = []
#     printList = []

#     for dict in lst:
#         result = []
#         for key in dict:
#             value = str(dict[key]) if dict[key] is None else dict[key]
#             result.append((key, ':', value))
#         resultList.append(result)

#     for lst in resultList:
#         for tpl in lst:
#             j = ''.join(tpl)
#             jList = '\n'.join(j)
#         printList.append(jList)
#     return printList

    
# result = createUser(user_data)
# finalResult = makeResult(result)
# print(finalResult)



# def isValidation(lst):
#     finalInvalidList = []
    
#     for i in lst:
#         invalidList = []
#         isBlack = False

#         if i['company'] in black_list:
#             isBlack = True
#             invalidList.append('blocked')
#         if 'blocked' in invalidList:
#             finalInvalidList.append('blocked')
#         if isBlack:
#             continue

#         if i['blood_group'] not in blood_types:
#             invalidList.append('blood_group')
#         if '@' not in i['mail']:
#             invalidList.append('mail')
#         if len(i['website']) < 1:
#             invalidList.append('website')
#         if len(i['name']) < 2 or len(i['name']) > 30:
#             invalidList.append('name')
        
#         if invalidList:
#             finalInvalidList.append((False, invalidList))

#     if len(invalidList) == 0:
#         return True
#     else:
#         return finalInvalidList
# def createUser(lst):
#     userDataCopy = copy.deepcopy(lst)  # 원본 보호를 위한 복사
#     userList = []  # 최종 결과 리스트
#     isValResult = isValidation(lst)  # 유효성 검사 결과 가져오기

#     if isValResult == True:  # 유효성 검사 통과
#         userList.extend(userDataCopy)  # 모든 유저를 그대로 추가

#     elif isValResult:  # 유효성 검사 실패한 경우
#         for user, data in zip(userDataCopy, isValResult):  # 유저와 결과 매칭
#             if isinstance(data, tuple) and data[0] is False:  # 실패한 유저 처리
#                 for key in data[1]:  # 실패한 필드만 값 수정
#                     if key in user:
#                         user[key] = None
#                 userList.append(user)  # 수정된 유저 추가
#             elif data == "blocked":  # 블록된 유저는 추가하지 않음
#                 continue

#     return userList
    
# [(False, ['blood_group']), 'blocked', 'blocked', 'blocked', 'blocked']


                
                 
            
