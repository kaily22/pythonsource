from os import write
import requests
from bs4 import BeautifulSoup
from requests.models import Response

url = 'https://news.v.daum.net/v/20210714085530597'

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

#print(soup.prettify())

#뉴스 제목 가져오기
#title = soup.find("h3")
title = soup.select_one("h3")
print("title : {}".format(title.string))

#작성자 가져오기
#writer = soup.find("span", class_="txt_info")
writer = soup.select_one("span.txt_info")
print("writer : {}".format(writer.string))

#작성 시간 가져오기
#date = soup.find("span", class_="num_date")
date_time = soup.select_one("span.num_date")
print("작성날짜 및 시간 : {}".format(date_time.text))

#첫 번째 문단 가져오기
#content = soup.find("p")
content = soup.select_one("p")
print("내용 : {}".format(content.string))

#두번째 문단 가져오기 
#content2 = soup.find("p",{"dmcf-pid" : "klpI5mddxe"})
content2 = soup.select_one("p[dmcf-pid='klpI5mddxe']")
print("내용2 : {}".format(content2.string))
