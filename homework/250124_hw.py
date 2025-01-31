# # ------------------------------------------
# #  hs_5_2
# def count_character(my_str, my_alpha):
#     return str(my_str).count(my_alpha)


# result = count_character("Hello, World!", "o")
# print(result)  # 2





# # ------------------------------------------
# #  hs_5_4
# def find_min_max(list):
#     return min(list), max(list)


# result = find_min_max([3, 1, 7, 2, 5])
# print(result)  # (1, 7)





# # ------------------------------------------
# #  ws_5_4
# def capitalize_words(my_str):
#     return str(my_str).title()


# result = capitalize_words("hello, world!")
# print(result)





# # ------------------------------------------
# #  ws_5_5


# def even_elements(list):
#     popList = []
#     i = 0
#     for num in list:
#         if num % 2 == 0:
#             return list.index(num)
        
#         popList.append(list.pop(i))
#         return popList
            
# def even_elements(list):
#     evenList = []
#     i = 0
#     while i < len(list): 
#         if list[i] % 2 == 0:
#             evenList.append(list.pop(i))
#         else :
#             i += 1
#     return evenList

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)





# # ------------------------------------------
# #  ws_5_3
# def sort_tuple(tpl):
#     new_tpl = tuple(sorted(tpl))
    
#     return new_tpl


# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)





# # ------------------------------------------
# #  ws_5_3
# def remove_duplicates(lst):
#     new_lst = list(set(lst))
#     return new_lst

# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)


# def remove_duplicates(lst):
#     newList = []
#     for num in lst:
#         if num in newList:
#             continue  # 이미 newList에 있으면 추가하지 않음
#         elif lst.count(num) > 1:
#             newList.append(num)  # 중복되는 숫자 중 하나를 추가
#         else:
#             newList.append(num)  # 중복되지 않은 숫자를 추가
#     return newList

# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)





# # ------------------------------------------
# #  ws_5_c
def restructure_word(word, arr):
    for w in word:
        if w.isdecimal() == True:
            for i in range(int(w)):
                arr.pop()
        else:
            arr.remove(w)
    return arr

        
        

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []


    
for oWord in original_word:
    arr.extend(oWord)
print(arr)
    
result = restructure_word(word, arr)
print(result)

print(''.join(result))