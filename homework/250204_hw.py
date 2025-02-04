# ------------------------------------------
# ws_6_3
# def intersection_sets(set1, set2):
#     intset = set1 & set2
#     if intset == set():
#         print('공통 요소가 없습니다.')
#     else:
#         return len(intset), intset
#     return len(intset), intset


# result = intersection_sets({1, 2, 3}, {3, 4, 5})
# print(result)  # (1, {3})

# result = intersection_sets({1, 2}, {3, 4})
# print(result)  # (0, set())
# # 출력: 공통 요소가 없습니다





# ------------------------------------------
# ws_6_4
# def get_keys_from_dict(dictionary):
#     return list(dictionary.keys())

# def get_all_keys_from_dict(dictionary):
#     keyList = []
#     for key, value in dictionary.items():
#         if type(value) is dict:
#             keyList.append(key)
#             keyList.extend(list(value.keys()))
#         elif type(value) is not dict:
#             keyList.append(key)
#     return keyList
        

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_keys_from_dict(my_dict)
# print(result)  # ['name', 'age']

# my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
# result = get_all_keys_from_dict(my_dict)
# print(result)  # ['person', 'name', 'age', 'location']





# ------------------------------------------
# ws_6_5
# def ordered_difference_sets(set1, set2):
#     result1 = set1 - set2
#     result2 = set2 - set1
#     if len(result1) <= len(result2):
#         return result1, result2
#     else:
#         return result2, result1

# # 예시 실행
# result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
# print("결과:", result)  # 출력: ({1, 2}, {5, 6})

# result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
# print("결과:", result)  # 출력: (set(), {4})





# ------------------------------------------
# hw_6_2
# def list_to_set(lst):
#     return set(lst)

# my_list = [1, 3, 1, 0, 4, 6, 0]
# print(list_to_set(my_list))


# def remove_duplicates_to_set(lst):
#     fine_set = set()
#     for num in lst:
#         if num not in fine_set:
#             fine_set.add(num)
#     return fine_set
    
# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)






# ------------------------------------------
# hw_6_4
def add_item_to_dict(dictionary, key, value):
    new_dict = dictionary.copy()
    new_dict.setdefault(key, value)

    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)