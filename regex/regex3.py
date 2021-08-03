import re


print("[] : 괄호 안에 들어가는 문자가 들어있는 패턴")
pattern = re.compile("[abcdefgABCDEFG")
print(pattern.search("a1234"))
print(pattern.search("abc1234"))
print(pattern.search("abcz1234"))
print(pattern.search("abAB1234"))