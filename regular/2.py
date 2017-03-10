import re

story = '''Born to the prestigious Crownguards, the paragon family of Demacian service,
Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately
took to the advanced education and lavish parties required of families as high profile
as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted.
She could play tricks that made people believe they had seen things that did not actually exist.
She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells
 after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian
  government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic,
she was discovered to possess a unique command over the powers of light.
The young Lux viewed this as a great gift, something for her to embrace and use in the name of good.
Realizing her unique skills, the Demacian military recruited and trained her in covert operations.
She quickly became renowned for her daring achievements; the most dangerous of which found her deep
in the chambers of the Noxian High Command. She extracted valuable inside information about
the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However,
 reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was
 the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an
  inspiration for all of Demacia.'''

print(re.findall('Lux', story))
print(re.findall('Lux|her|she', story))
print(re.findall('[Ll]ux | [Hh]er | [Ss]he',story)) # 대소문자 구분
print(re.findall('^Born', story))
print(re.findall('^Lux', story))
print(re.findall('Demacia$', story))
print(re.findall('Demacia\.$', story))

print(re.findall('was',story))
print(re.findall('(?<=she) was',story)) # she 가 있을 경우에만 was를 검색

s= re.search(r'\w+\s(was)',story)
print(s.group())
print(s.group(0))
print(s.group(1))

m = re.search(r'(?P<before>\w+)\s+(?P<was>was)\s+(?P<after>\w+)', story)
print(m.groups())
print(m.group('before'))
print(m.group('was'))
print(m.group('after'))

p = re.compile (r'\a{\w{3}',story)
