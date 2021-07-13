from bs4 import BeautifulSoup

with open("./beautifulsoup/dormouse.html","r") as f:
    html = f.read()

soup = BeautifulSoup(html,"html.parser")

print("--find()로 찾기")

title = soup.find("title")

# print("title >> {}".format(title))
# print("title 내용 >> {}".format(title.string))
# print("title 부모 태그 >> {} ".format(title.parent))

# h1 = soup.find("h1")
# print("h1 >> {}".format(h1))
# print("h1 내용 >> {}".format(h1.string))

#첫번째 p
# p1 = soup.find("p")
# print("p >> {}".format(p1))
# print("p 내용 >> {}".format(p1.get_text()))
# print("p 클래스명 >> {}".format(p1['class']))

#두번째 p
p2 = soup.find("p",class="story")
print("p >> {}".format(p2))
print("p 내용 >> {}".format(p2.get_text()))
print("p 클래스명 >> {}".format(p2['class']))

#a태그
# a1 = soup.a
# print("a >> {} ".format(a1))
# print("a 태그 내용 >> {}".format(a1.string))

# a2 = a1.find_next_sibling("a")
# print("a >> {}".format(a2))
# print("a 태그 내용 >> {}".format(a2.string))