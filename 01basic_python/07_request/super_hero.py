import requests


url = 'https://superheroapi.com/api/2619421814940190/search/'
names_characters = [{'name': 'Hulk'}, {'name': 'Captain_America'}, {'name': 'Thanos'}]
def connect_url(main_url):
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }
    session = requests.Session()
    req = session.get(main_url, headers=headers)
    if req.status_code == 200:
        return True
    else:
        print('Error!!!')

def super_hero_func(hero_url, name_hero):
    new_dict = {}
    if connect_url(url):
        for names in name_hero:
            main_url = hero_url + names['name']
            response =  requests.get(main_url)
            data = response.json()
            # with open("super_hero.txt", "a", encoding="utf-8") as file:
            #     json.dump(data, file, indent=2, ensure_ascii=False)
            intelligence_hero = int(data['results'][0]['powerstats']['intelligence'])
            keys = names['name']
            new_dict[keys] = intelligence_hero
            most_intelligent = max(new_dict, key=new_dict.get)
        print('Most intelligent: ', most_intelligent, 'IQ:', new_dict[keys])

def main():
    super_hero_func(url, names_characters)

if __name__ == '__main__':
    main()



