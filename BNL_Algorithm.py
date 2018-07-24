# data set 만들기 [가격 , 해변으로부터의 거리]
data_set = [[45, 90], [35, 92], [43, 90], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
# 크기가 3인 window set 만들기
window_set = [i for i in range(3)]
# 크기가 ? 인 temp set 만들기
temp_set = [0]

first_data = [0]
second_data = [0]
skyline = []

SkylineOpOutput = []
TempFile = []
MainMemo = []
CountIn = 0
CountOut = 0
for i in range(len(data_set)):
