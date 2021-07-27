'''
Выведите на экран все уникальные гео-ID из значений словаря ids.
Т.е. список вида [213, 15, 54, 119, 98, 35]
'''
from pprint import pprint

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
user_set = set()
for i in list(ids.values()):
    for j in i:
        user_set.add(j)
print('Уникальные гео-ID из значений заданного словаря -', *user_set)
