import urllib.request as req

#좋아하는 연예인 사진 가져오기

file_url = "http://img.sportsworldi.com/content/image/2021/05/09/20210509508487.PNG"


html_url ="http://www.google.com"

#다운 받을 경로
save_img = "c:/sohee.jpg"
save_html="c:/googlephoto.html"

try:
    file1, header1 = req.urlretrieve(file_url,save_img)
    file2, header2 = req.urlretrieve(html_url,save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("다운로드 성공!")
