import requests
from bs4 import BeautifulSoup
import urllib.request

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = requests.get('https://music.bugs.co.kr/chart/track/week/total',headers = header)
soup = BeautifulSoup(req.content,'html.parser')
bugscharts = soup.select('#CHARTweek > table > tbody > tr')


# #CHARTweek > table > tbody > tr:nth-child(1) > td:nth-child(5) > a > img
for i, bugschart in enumerate(bugscharts, 1):
     img = bugschart.select_one("a.thumbnail > img")
     img_src = img.attrs['src']
     #이미지 저장하기

     urllib.request.urlretrieve(img_src, f'media\Bugs\Bugs{i}.jpg')