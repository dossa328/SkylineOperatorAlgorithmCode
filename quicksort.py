data_set = [1, 4, 2, 5, 7, 6, 8, 3]


def Quicksort(data_set, startidx, endidx):
    if startidx < endidx:
        q = partition(data_set, startidx, endidx)
        Quicksort(data_set, startidx, q - 1)
        Quicksort(data_set, q + 1, endidx)
        # 퀵 소트 호출 및 partition 호출
        # 우리가 찾고자 하는 기준값을 계산 할 수 있음.
    return data_set

def partition(sub_set, startidx, endidx):
    pivot = sub_set[endidx]
    i = startidx-1
    #for val in sub_data_set:
    for val in range(startidx, endidx):
        if sub_set[val] != sub_set[endidx]:
            if sub_set[val] <= pivot:
                i = i + 1
                sub_set[val], sub_set[i] = sub_set[i], sub_set[val]

            # swap
                #swap 과정에서 문제 있음. 인덱스 이동 다시 볼것.
    sub_set[endidx], sub_set[i+1] = sub_set[i+1], sub_set[endidx]

    return i + 1
    # 파티셔닝


print(Quicksort(data_set, 0, len(data_set) - 1))
