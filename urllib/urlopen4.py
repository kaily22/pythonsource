import urllib.request as req

#urlopen = 메모리에 내용을 올려놓고 분석

#파일 url
file_url = ["https://www.daum/net",
"https://search1.kakaocdn.net/argon/0x200_85_hr/77obNfwaRKN"
]

#저장할 경로 지정
path_list =["c:/daum1.html","c:/dog1.jpg"]

for i ,url in enumerate(file_url):
    try:
        response = req.urlopen(url)
        contents = response.read()

        #파일 저장 (wb-write byte)
        with open(path_list[i],"wb") as c:
             c.write(contents)
    except:
        print("에러발생")
    else:
        print("headers info-{}:{}".format(i,response.info()))
        print()
        print("-----------------------------------------------")
        
        print(contents[:3000])


