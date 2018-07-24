# 가장 기초적인 Skyline set 구하기
# data set 만들기 [가격 , 해변으로부터의 거리]
data_set = [[45, 90], [35, 92], [43, 90], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
first_data = [0]
second_data = [0]
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
            if skyline.__contains__(first_data):
                pass
            else:
                skyline.append(first_data)
        else:
            if skyline.__contains__(first_data):
                skyline.remove(first_data)
                break
print(skyline)
