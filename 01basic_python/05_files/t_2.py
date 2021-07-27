from pprint import pprint
import os


keys = []
values = []
for file in os.listdir("dz_file"):
    if file.endswith(".txt"):
        file_path = (os.path.join("dz_file", file))
        with open(file_path, encoding='utf-8') as f:
            file_n = f.readlines()
            max_len = len(file_n)
            keys.append(max_len)
            values.append(file)
            dict_path = dict(zip(keys, values))
sorted_list = sorted(dict_path.items())

with open('itog.txt', 'w', encoding='utf-8') as fw:
    for file_name in sorted_list:
        file_path = (os.path.join("dz_file", file_name[1]))
        with open(file_path, encoding='utf-8') as fr:
            file_read = fr.read()
            fw.write(file_name[1] + '\n' + str(file_name[0]) + '\n' + file_read + '\n')
