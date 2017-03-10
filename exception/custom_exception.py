import re

class nomatchedException(Exception):
    def __init__(self,re_pattern=None,source=None):
        # 만약 인자로 주어진 re_pattern 객체가
        #re.-pattern
        self.pattern = re_pattern
        self.source = source

    def __str__(self):
        print('Not matched Exception')

def test_function():
    raise nomatchedException()

def search_from_source(pattern,source):
    m = re.search(pattern,source)
    if m:
        return m
    else:
        raise  nomatchedException(pattern,source)

try:
    source = 'Luxm thoe lady of Luminocity'
    pattern = re.compile('Laddyyyyy')
    search_from_source(pattern,source)

except nomatchedException as e:
    print(e)

test_function()
print('--pattern ')