sample_list = ['apple','banana','melon']
sample_dict={
    'game':['lol','starcraft'],
    'food':['hamberger,''pizza'],
    'color':['red','green','blue']
}



try:
    print(sample_list[2])
    print(sample_dict['fruits'])
except:
    print('리스트 초과')

print('--Exception__')
try:
    print(sample_list[2])
    print(sample_dict'fruits')
except IndexError:
    print('리스트 인덱스 에러')
except KeyError:
    print('딕셔너리 키 에러 ')

print('--program terminate')