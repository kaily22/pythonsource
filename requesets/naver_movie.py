import requests

#urlparse2.py
search_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&"

param = {"query" : "영화"}

with requests.Session() as s:
    r = s.get(search_url,params=param)
    print(r.text[130000:150000])