import requests
import re
from  bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
}

r = requests.get('https://gaokao.chsi.com.cn/zyk/pub/myd/schAppraisalTop.action',headers = headers)
# response = requests.get('https://gaokao.chsi.com.cn/')

soup = BeautifulSoup(r.content, 'lxml')

print(soup)