import requests
from bs4 import BeautifulSoup
import urllib.request

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = requests.get('https://www.melon.com/chart/week/index.htm',headers = header)
soup = BeautifulSoup(req.content,'html.parser')
meloncharts = soup.select('table > tbody > tr')

# #lst50 > td:nth-child(4) > div > a > img
for i, melonchart in enumerate(meloncharts, 1):
     img = melonchart.select_one("div.wrap > a.image_typeAll > img")
     img_src = img.attrs['src']
     #이미지 저장하기

     urllib.request.urlretrieve(img_src, f'media\melon\melon{i}.jpg')