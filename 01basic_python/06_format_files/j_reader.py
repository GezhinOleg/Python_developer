import json
import collections
from pprint import pprint

def read_json(file_path, max_len_word = 6, top_words = 10):
    with open(file_path, encoding = 'utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            # С помощью List Comprehension перебераем все полученные слова и определяем их длину
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        pprint(counter_words.most_common(top_words))
'''
Для решения задачи мы использовали из модуля collections класс Counter.
Он автоматически подсчитывает количество вхождений слов в списке. И с помощью
метода most_common (13 строка) можно получить топ нужных слов. Также обратите
внимание, что добавился ещё один параметр top_words для удобного изменения
нужного количества популярных слов.
'''

if __name__ == '__main__':
    read_json('newsafr.json')
