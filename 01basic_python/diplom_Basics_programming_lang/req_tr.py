import requests
import json

class YaDisk:
    def __init__(self, token: str):
        self.token = token






if __name__ == '__main__':
    with open('token_yd.txt', 'r', encoding='utf-8') as file_object:
        token_yd = file_object.read().strip()
    uploader = YaDisk(token = token_yd)

