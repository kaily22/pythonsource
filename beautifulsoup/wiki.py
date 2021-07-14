import requests

from bs4 import BeautifulSoup

url="https://ko.wikipedia.org/wiki/서울_지하철"

response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

#print(soup.prettify())


#첫 번째 이미지 태그 가져오기
##mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img
first_img = soup.select_one("div.mw-parser-output > table img")
print(first_img)

#mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img
second_img = soup.select_one("div.thumbinner img")
print(second_img)

#src 속성 값 출력
print("img src ", first_img["src"])
print("img2 src ",second_img["src"])

# a 링크의 갯수?
links = soup.select("a")
print("link count : ", len(links))