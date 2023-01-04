import requests
from bs4 import BeautifulSoup
import json

url = 'https://api.joara.com/v1/best/book.joa?api_key=mw_8ba234e7801ba288554ca07ae44c7&ver=2.6.3&device=mw&deviceuid=e11ac5a168884f4b16237c319532e267ce09c70db2d4d760fd1a7b6b9a1f1e64&devicetoken=mw&token=2030b91833814986c4b07b7dd00af21b&category=22&best=today&store=&orderby=cnt_best&offset=20&page=1'

res = requests.get(url)

html = res.text

soup = BeautifulSoup(html, 'html.parser')

dict_result = soup.text

book_list = []

book_list.append(json.loads(dict_result))


with open('joara.json', 'w', encoding='utf-8') as file:
    json.dump(book_list, file, ensure_ascii=False, indent="\t")
