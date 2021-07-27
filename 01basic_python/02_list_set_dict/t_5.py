'''
Напишите код для преобразования произвольного списка вида
['2018-01-01', 'yandex', 'cpc', 100]
(он может быть любой длины) в словарь
{'2018-01-01': {'yandex': {'cpc': 100}}}
'''
source_lst = ['2018-01-01', 'yandex', 'cpc', 100]

finish_dict = {source_lst[-2]: source_lst[-1]}
for i in source_lst[:-2][::-1]:
    finish_dict = {i: finish_dict}
print(finish_dict)
