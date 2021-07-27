from pprint import pprint
with open('recipes.txt', encoding='utf-8') as f:
    file = f.readlines()
    max_len = len(file)
    ingr_dict = {}
    cook_book = {}
    key = file[0].strip()
    cook_book[key] = []
    keys = ['ingredient_name', 'quantity', 'measure']


    print(cook_book)
