DEBUG=False
source = [9,1,6,8,4,3,2,0,5,7]
length = len(source)

    # 일단 모든 문자열을 순회한다.
    def selection_sort():
        for index in range(length):
            cur_min_index = index

            if DEBUG:
                print('loop{}, value : {}'.format(index, source[index]))

            #비교하려는 문자 다음부분 부터 순회한다.
            for inner_index in range(index +1, length):
                if DEBUG:
                    print('loop{}, value : {}'.format(inner_index,source[inner_index]))
                    print('min_value : {}, cur_value : {}'.format(source[cur_min_index],source[inner_index]))

                    # 만약 현재값이 cur_min_index의 값보다 작을 경우
                    # 해당 인덱스값 (inner _index)를 cur_min_index에 기록한다.
            if source[cur_min_index] > source[inner_index]:
                cur_min_index = inner_index
                if DEBUG:
                    print('change min value({}), index : {}'.format(source[cur_min_index],cur_min_index))
                    #만약 cur_min_index값이 바뀌었다면
                    #기준에 index값이었으나 inner_index에서 더작은값이 나타난 경우

        if cur_min_index != index:
        #현재 index와 커민 인덱스를 바꿔준다.
            source[cur_min_index],source[index] = source[index],source[cur_min_index]


print(source)

selection_sort()
