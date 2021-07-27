import json
import requests
import datetime
import time

def main():

    delta = datetime.timedelta(days = 1)
    today = datetime.datetime.today()
    fromdate = datetime.datetime(today.year, today.month, today.day) - delta
    fromdate_unixtime = round(time.mktime(fromdate.timetuple()))
    params = {
        'pagesize': 100,
        'page': 1,
        'fromdate': fromdate_unixtime,
        'order': 'desc',
        'sort': 'activity',
        'tagged': 'Python',
        'site': 'stackoverflow'
    }

    has_more = True
    questions_list = []
    while has_more:
        api_url = f'https://api.stackexchange.com/2.2/search/advanced'
        response = requests.get(api_url, params=params).text
        # print(response)
        questions_db = json.loads(response)
        for question in questions_db['items']:
            questions_list.append(question['title'])
        has_more = questions_db['has_more']
        params['page'] += 1

    for question in questions_list:
        print(question)

if __name__ == '__main__':
    main()