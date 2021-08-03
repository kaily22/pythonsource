import requests
import pprint

naver_open_api = "https://openapi.naver.com/v1/search/news.json"
client_id="GXNDKs7u1YnIflOKRYos"
client_secret = "tnBVcx2EaX"

headers = {
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret" : client_secret
}

param = {
    "query":"아이폰",
    "sort":"sim"
}

response = requests.get(naver_open_api,headers=headers, params=param)

#print(response)

if response.status_code == 200:
    data = response.json() #json.loads()

    # print(data["items"][0])
    # print(data["items"][0]["link"])

    print()
    # pprint.pprint(data['items'])

    for idx,item in enumerate(data['items'],1):
        print(idx,item['title'],item['link'])
    