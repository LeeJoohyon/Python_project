import re
source = 'Lux, the Lady of Luminosity'
# match -> 시작부분부터 일치하는 패턴만 찾는다
# search -> 첫번째 일치하는 패턴을 찾는다
# findall -> 복수개의 일치하는 패턴을 찾는다 -> list로 리턴해준다
# split -> 문자열을 기준 문자로 구분하여 list로 리턴해준다
# replace
# group -> 일치하는 패턴을 찾아준다
# . -> 문자 1개를 의미한다
# * -> 해당 패턴이 0회 이상 올 수 있다는 의미

print('--p1--')
p1 = re.compile('Lux')
m1 = re.match(p1, source)
if m1:
   print(m1.group())

print('--p2--') # match 는 시작부분부터 일치하는 패턴을 찾기 때문에 못찾는다
p2 = re.compile('Lady')
m2 = re.match(p2, source)
if m2:
   print(m2.group())

print('--p3--')
p3 = re.compile('.*Lady') # 이렇게 해줘야 match 가 찾을 수 있다 (p2해결책)
m3 = re.match(p3,source)
if m3:
   print(m3.group())

print('--p4--')
p4 = re.compile('Lady')
m4 = re.search(p4, source)
if m4:
   print(m4.group())

print('--p5--')
p5 = re.compile('y')
m5 = re.findall(p5, source)
if m4:
   print(m5)

print('--p6--')
p6 = re.compile('y..') # y o가 리턴된다
m6 = re.findall(p6, source)
if m4:
   print(m6)

print('--p7--')
s2 = '민아 헤리 소진 유라'
s2_list = s2.split(',')
print(s2_list)

print('--p8--')
m = re.split('.o', source)
print(m)

print('--p9--')
s2 = source. replace('L', 'A')
print(s2)

print('--p10--')
m = re.sub('L', 'A',source)
print(m)

import string
printable = string.printable
printable += "가나다라마바사아자카타파하"
print(printable)

print('--string1--')
m = re.findall('\w', printable) # 문자
print(m)

print('--string2--')
m = re.findall('\W', printable) # 비문자
print(m)

print('--string3--')
m = re.findall('\d', printable) # 숫자
print(m)

print('--string4--')
m = re.findall('\D', printable) # 비숫자
print(m)

print('--string5--')
m = re.findall('\s', printable) # 공백
print(m)

print('--string6--')
m = re.findall('\S', printable) # 비공백
print(m)

print('--string7--')
m = re.findall('\b', printable) # 단어 경계(\w 와 \W 의 경계
print(m)

print('--string8--')
m = re.findall('\B', printable) # 비단어 경계
print(m)

[11:56]
