# 가장 기초적인 Skyline set 구하기
# data set 만들기 [가격 , 해변으로부터의 거리]
data_set = [[45, 90], [35, 92], [43, 90], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
#data_set = [[1, 8], [2, 7], [3, 6], [1.5, 6]]
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

# 1개 data set 을 입력받음 -> first_data
# 자신을 포함한 data 를 입력 받음 -> second_data
# first_data 와 second_data를 비교함


for first_data in data_set:
    for second_data in data_set:
        # 만약 first_data가 second_data에 의해 dominated 되지 않는다면..
        if not dominated(first_data, second_data):
            # skyline list 내에 first data가 존재한다면 pass
            if skyline.__contains__(first_data):
                pass
            # 아니라면 skyline list에 first_data를 append
            else:
                skyline.append(first_data)
        # 그 외의 상황이라면
        else:
            # skyline list 내에 first data가 존재한다면
            if skyline.__contains__(first_data):
                # skyline list 내에 들어있는 first_data를 삭제, 이 데이터는 skyline set이 될수 없기 때문
                skyline.remove(first_data)
                # 이후 break한 후 다음 데이터(first_data)로 넘어간다.
                break

print(skyline)
