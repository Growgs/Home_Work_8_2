import requests

from config import TOKEN

from pathlib import Path

class YaUploader:

    def __init__(self, token):
        self.token = token


    def upload(self, file_path):
        self.file_path = file_path
        self.token = token
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {TOKEN}'}
        params = {'path': self.file_path.name, 'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params).json()['href']
        download_res = requests.put(response, data=open(self.file_path.name, 'rb'))
        download_res.raise_for_status()
        if download_res.ok:
            return 'Файл успешно загружен на Я.Диск'
        return 'Ошибка загрузки'


if __name__ == '__main__':
    file_path = Path('/1.txt')
    token: str = TOKEN
    uploader = YaUploader(token)
    #
    uploader.upload(file_path)
    print(uploader.upload(file_path))