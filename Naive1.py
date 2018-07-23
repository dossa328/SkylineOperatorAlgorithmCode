# data set 만들기 [가격 , 해변으로부터의 거리]
data_set = [[45, 90], [35, 92], [43, 90]]
# [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
# 크기가 3인 window set 만들기
data1 = [i for i in range(1)]
# 크기가 ? 인 temp set 만들기
first_data = [0]
second_data = [0]
temp = [0]
ck = 0
dom = []
skyline = []


def dominated(looser, winner):
    dim = len(looser)

    # as good or better in all dimensions
    for i in range(dim):
        if winner[i] > looser[i]:
            return False

    # better in at least one dimension
    for i in range(dim):
        if winner[i] < looser[i]:
            return True

    return False


for first_data in data_set:
    for second_data in data_set:
        if not dominated(first_data, second_data):
            skyline.append(first_data)
        else:
            if skyline.__contains__(first_data):
                delete = len(skyline)
                for i in range(delete):
                    skyline.remove(first_data)
                break

print(skyline)