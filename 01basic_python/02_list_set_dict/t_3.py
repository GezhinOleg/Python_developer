'''
Дан список поисковых запросов. Получить распределение количества слов в них.
Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
'''
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
count_str = []
for i in queries:
    count_str.append(len(i.split(' ')))

percent_dict = {}
for j in count_str:
    if j in percent_dict:
        percent_dict[j] += 1
    else:
        percent_dict[j] = 1

for item in sorted(percent_dict):
    print("'%d':%d проц" % (item, (percent_dict[item]*100/len(count_str))))

# print(sorted(count_str))
