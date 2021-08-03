#정규 표현식
#특정한 패턴과 일치하는 문자열을 검색, 치환 ,제거
#정규 표현식의 도움 없이 패턴을 찾을 순 있지만, 불완전 하거나 작업의 cost가 높음

import re

#search()

#패턴 설정 
#compile() : 정규표현식
pattern = re.compile('D.A') # '.' 어떤 문자열도 상관없이

result = pattern.search('DAA') #<re.Match object; span=(0, 3), match='DAA'>
print(result)
#print(result.start(),result.end(),result.group())

print("\n원본 문자열에 일치하는 패턴이 없느 경우")
print(pattern.search('D00A')) #None
print(pattern.search('DA'))
print(pattern.search('d0A'))

print(pattern.search("d0A D1A 0111"))  #<re.Match object; span=(4, 7), match='D1A'>