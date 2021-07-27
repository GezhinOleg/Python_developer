import requests
import json
import datetime
import os
import time
from tqdm import tqdm


def write_json(data):
    with open('response.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


# selecting the largest images
def get_largest(size_dict):
    if size_dict['width'] >= size_dict['height']:
        return size_dict['width']
    else:
        return size_dict['height']


# uploading and renaming photos
def download_photo(url_photo, file_name):
    r_photo = requests.get(url_photo)
    with open(file_name, 'bw') as file:
        file.write(r_photo.content)


# main function
def main():
    with open('token_vk.txt', 'r', encoding='utf-8') as file_object:
        token_vk = file_object.read().strip()

    URL = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': '552934290',
        'access_token': token_vk,
        'album_id': 'profile',
        'extended': '1',
        'v': '5.130'
    }
    res = requests.get(URL, params=params)
    write_json(res.json())
    photos = res.json()['response']['items']
    file_dict = {}
    i = 0
    for item_s in photos:
        size_s = item_s['sizes']
        max_size_url = max(size_s, key=get_largest)['url']
        f_likes = item_s['likes']
        count_s = str(f_likes['count'])
        f_date = item_s['date']
        file_name = datetime.datetime.fromtimestamp(f_date).strftime('%M_%S') + 'like' + count_s + '.jpeg'
        w = max_size_url.split('=')[1]
        size_p = w.split('&')[0]
        file_dict[i] = {'name': file_name, 'size': size_p}
        i += 1
        download_photo(max_size_url, file_name)
    with open('download.json', 'w', encoding='utf-8') as file:
        json.dump(file_dict, file, indent=2, ensure_ascii=False)
    #     ______________________________________________________________________


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": path, "overwrite": "true"}
        response = requests.put(folder_url, headers=headers, params=params)
        return response.json()

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path, filename):
        href = self._get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    main()
    uploader = YaUploader(token='')
    r = uploader.create_folder("Pict/")
    for file in os.listdir():
        if file.endswith(".jpeg"):
            for i in tqdm(file):
                time.sleep(0.5)
            filename = file
            result = uploader.upload("Pict/" + filename, filename)
