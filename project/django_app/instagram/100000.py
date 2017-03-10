import time

BIG_NUM = 100000

def func_loop():
    char = ''
    for i in range(100000):
        char += 'a'
        return char

def func_list():
    l = []
    for i in range(BIG_NUM):
        l.append('a')
        return ''.join(l)

def func_comprehension():
    return ''.join(['a'for i in range(BIG_NUM)])