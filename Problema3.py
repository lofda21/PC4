import requests
import os
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

URL = 'https://plus.unsplash.com/premium_photo-1681882526882-c2da94c47783?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80'

def main():
    path_descarga = './descargas'
    if not os.path.isdir(path_descarga):
        os.mkdir(path_descarga)
    response = requests.get(URL, headers=HEADERS, timeout=10)
    with open(f'{path_descarga}/perrito.jpg', 'wb') as f:
        f.write(response.content)
    print('Descarga finalizada!!')
if __name__ == '__main__':
    main()