'''
Я работаю секретарем и мне постоянно приходят различные документы.
Я должен быть очень внимателен чтобы не потерять ни один документ.
Каталог документов хранится в следующем виде:
      documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
Перечень полок, на которых находятся документы хранится в следующем виде:
      directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
a – add – команда, которая добавит новый документ в каталог и в перечень
    полок, спросив его номер, тип, имя владельца и номер полки, на котором он
    будет храниться. Корректно обработайте ситуацию, когда пользователь
    будет пытаться добавить документ на несуществующую полку.

Внимание: p, s, l, a - это пользовательские команды,
а не названия функций. Функции должны иметь выразительное
название, передающие её действие.

d – delete – команда, которая спросит номер документа и удалит его
    из каталога и из перечня полок. Предусмотрите сценарий, когда
    пользователь вводит несуществующий документ;
m – move – команда, которая спросит номер документа и целевую полку
    и переместит его с текущей полки на целевую. Корректно обработайте
    кейсы, когда пользователь пытается переместить несуществующий
    документ или переместить документ на несуществующую полку;
as – add shelf – команда, которая спросит номер новой полки и
    добавит ее в перечень. Предусмотрите случай, когда пользователь
    добавляет полку, которая уже существует.;
'''
documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def Person_Document(doc_list):
    result = 'Извините, введенный номер в базе отсутствует!'
    doc_input = input('Введите номер документа:')
    for i in doc_list:
        if doc_input == i['number']:
            result = i['name']
    return result

def Shelf_Document(shelf):
    number_doc = input('Введите номер документа: ')
    result = 'Извините, введенный номер в базе отсутствует!'
    for shelf_l, doc in shelf.items():
        for j in doc:
            if number_doc == j:
                result =  f'Лежит на полке № {shelf_l}'
    return  result


def List_All_Document(doc_list):
    for doc in doc_list:
        print(doc['type'], '"', doc['number'], '"', '"', doc['name'], '"',)

def Add_Document(doc_list, doc_shelf):
    result = 'Введите правильный номер полки!'
    dict_person = dict()
    type_doc = input('Введите название документа: ')
    dict_person["type"] = type_doc
    number_doc = input('Введите номер документа: ')
    dict_person["number"] = number_doc
    name_doc = input('Введите фамилию имя: ')
    dict_person["name"] = name_doc
    doc_list.append(dict_person)

    number_shelf = input('Введите номер полки: ')
    for sh_k, sh_v in doc_shelf.items():
        if number_shelf == sh_k:
            sh_v.append(number_doc)
            result = ''
    print(result)
    for d_doc in doc_list:
        print(*d_doc.values())
    for shelf_l, sh_doc in doc_shelf.items():
        print(f'{shelf_l} - {sh_doc}')

def main():
    while True:
        print('Для работы с программой введите команды: p, s, l, a, d, m, as')
        user_input = input('Введите команду: ')
        if user_input == 'p':
            print(Person_Document(documents))
        elif user_input == 's':
            print(Shelf_Document(directories))
        elif user_input == 'l':
            List_All_Document(documents)
        elif user_input == 'a':
            Add_Document(documents, directories)
        elif user_input == 'd':
            Delete_Document(documents, directories)
        elif user_input == 'm':
            Movie_Document(documents, directories)
        elif user_input == 'as':
            Add_Shelf(documents, directories)
        elif user_input == 'quit':
            print('До свидания!')
            break
main()
