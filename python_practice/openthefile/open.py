skills = '''Iillumnination
light bidnding
prismatioc barrier
lucent siguralrity
final spark'''

info = 'minalksdfkljklsjdklfjslkdjfdlksdjlf'

len(skills)

f = open('skills.txt','wt')

f.write(skills)

f.close()
f = open('skills.txt','wt')

size = len(skills)
print(size)

offset = 0

chunk = 30

while True:
    if offset > size:
        break

    f.write(skills[offset:offset+chunk])
    offset += chunk

f.close()


