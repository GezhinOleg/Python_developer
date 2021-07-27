
from pprint import pprint
with open('recipes.txt', encoding='utf-8') as f:
    file = f.readlines()
    max_len = len(file)
    ingr_dict = {}
    cook_book = {}

    #Вариант с while
    i = 0
    while i < max_len:
        dish = file[i].strip()
        cook_book[dish] = []
        i += 1
        count = int(file[i].strip())
        for _ in range(count):
            i += 1
            ingr = file[i].strip().split(' | ')
            cook_book[dish] += [{'ingredient_name': ingr[0], 'quantity': int(ingr[1]), 'measure': ingr[2]}]
        i += 2


    #Вариант с for
    key = file[0].strip()
    ingr_dict[key] = []
    keys = ['ingredient_name', 'quantity', 'measure']
    for i in range(max_len):
        line = file[i].strip()

        if line == (''):
            key = file[i + 1].strip()
            ingr_dict[key] = []

        elif not line[0].isdigit() and line != key:
                values = line.split(' | ')
                values[1] = int(values[1])
                ingredient = dict(zip(keys, values))
                ingr_dict[key] += [ingredient]

pprint(ingr_dict)

def get_shop_list_by_dishes(dishes, person_count):
    value_dict = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            if value_dict.get(ingredient['ingredient_name']) is None:
                 value_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
            else:
                 value_dict[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
            key = ingredient['ingredient_name']
    pprint(value_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3)
