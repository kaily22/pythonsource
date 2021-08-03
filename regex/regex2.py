import re

print("**** 반복 *****")
print("? : 최소 0~최대 1")
pattern = re.compile("D?A") #D가 안나와도 되고, 있다면 D는 하나만 나오면 됨
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("AA"))
print("\n")
print("* : 최소 0~ 최대 무한대")
pattern = re.compile("D*A")
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.serach("AA"))
print(pattern.search("DDDDDDDDDDDDDA"))
print("\n")
print("{n} 사용법")
pattern = re.compile("AD{2}A")