data_set = [1, 4, 2, 5, 7, 6, 8, 3]
# data_set = [3, 6, 8, 9, 5, 6, 234, 5, 1, 33, 4, 16, 37, 49, 46, 7, 11, 34, 5, 6, 6777, 45, 33, 5, 56, 77]
# data_set = [13, 7, 6, 45, 21, 9, 101, 102]


# Quicksort 호출
def Quicksort(data_set, startidx, endidx):
    if startidx < endidx:
        q = partition(data_set, startidx, endidx)
        # 재귀적 호출
        Quicksort(data_set, startidx, q - 1)
        # 재귀적 호출
        Quicksort(data_set, q + 1, endidx)
        # 퀵 소트 호출 및 partition 호출
        # 우리가 찾고자 하는 기준값(pivot)을 계산 할 수 있음.
    return data_set


# partition 호출
# sub_set (부분 배열) 및, startidx, endidx ( 부분 배열의 처음과 끝 idx)
def partition(sub_set, startidx, endidx):
    # pivot 설정 / 여기선 배열의 마지막 부분을 pivot(기준점)으로 잡는다.
    pivot = sub_set[endidx]
    # i는 기준점을 이야기함, -1 부터 시작하는 이유는 각 부분배열의 startidx부터 시작할 경우 idx = 0은 비교 대상이 되지 않게됨
    i = startidx-1
    # for val 부터 부분 배열의 startidx ~ endidx 까지 for을 진행함
    for val in range(startidx, endidx):
        # 만약, 지금 비교하고 있는 element가 마지막(pivot)과 같지 않을때만 실행함. 같으면 정렬기준이 사라짐
        if sub_set[val] != sub_set[endidx]:
            # 위의 if가 참일경우, 비교 하고 있는 element가 pivot 보다 작거나 같을 경우
            if sub_set[val] <= pivot:
                # 기준이 되는 idx i의 값을 1 증가 시킨다.
                i = i + 1
                # 이때 비교 대상이 되는 sub_set[val]과 sub_set[i]를 swap한다.
                sub_set[val], sub_set[i] = sub_set[i], sub_set[val]
    sub_set[endidx], sub_set[i+1] = sub_set[i+1], sub_set[endidx]

    return i + 1
    # 파티셔닝


print(Quicksort(data_set, 0, len(data_set) - 1))
