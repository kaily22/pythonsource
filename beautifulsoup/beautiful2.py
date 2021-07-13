import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


userAgent = UserAgent()
headers = {
    "user-agent":userAgent.chrome
}

url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=103&oid=025&aid=0003117811"

response = requests.get(url,headers=headers)
#print(response.text)

soup = BeautifulSoup(response.text,'html.parser')

#find('h3',...) : 가장 처음에 만나는 태그 찾아주기
title = soup.find('h3',id="articleTitle")
print(title)
print(title.string)
print(title.get_text())
