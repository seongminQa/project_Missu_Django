import requests
from bs4 import BeautifulSoup
import urllib.request

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = requests.get('https://www.genie.co.kr/chart/genre?ditc=W&ymd=20230123&genrecode=M0100&pg=1',headers = header)

soup = BeautifulSoup(req.content,'html.parser')
geniecharts = soup.select('table.list-wrap > tbody > tr.list')

# #body-content > div.newest-list > div > table > tbody > tr.list.rank-3 > td:nth-child(3) > a > img
for i, geniechart in enumerate(geniecharts, 1):
     img = geniechart.select_one("a.cover > img")
     img_src = img.attrs['src']
     #이미지 저장하기
     genie_src = img_src.replace("//","https://")

     urllib.request.urlretrieve(genie_src, f'media\genie\genie{i}.jpg')