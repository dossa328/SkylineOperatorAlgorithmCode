# data set 만들기 [가격 , 해변으로부터의 거리]
data_set = [[45, 90], [35, 92], [43, 36], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
# 크기가 3인 window set 만들기
data1 = [i for i in range(1)]
# 크기가 ? 인 temp set 만들기
first_data = [0]
second_data = [0]
temp = [0]

dom = []
skyline = []
print(data_set[1][0])

first_data = data_set[0]
for i in range(len(data_set)):
    if first_data[0] > data_set[i][0] and first_data[1] > data_set[i][1]:
        first_data = data_set[i]

print(first_data)

for i in range(len(data_set)):
    if first_data[0] >= data_set[i][0] and first_data[1] <= data_set[i][1]:
        skyline.append(data_set[i])
    elif first_data[0] <= data_set[i][0] and first_data[1] >= data_set[i][1]:
        skyline.append(data_set[i])

print(skyline)
#for i in range(len(data_set)):
#temp = (min(data_set))
'''
first_data = data_set[0]
second_data = data_set[0]

print(first_data)
print(second_data)

for i in range(len(data_set)):
    if first_data[0] > data_set[i][0]:
        first_data = data_set[i]

print(first_data)

for i in range(len(data_set)):
    if second_data[1] > data_set[i][1]:
        second_data = data_set[i]

print(second_data)

print(min(data_set))
'''
# ds의 첫번째 데이터를 ws로 보냄
'''
window_set[0] = data_set[0]
for i in range(len(data_set)):
    if data_set[i][0] > window_set[0][0] and data_set[i][1] > window_set[0][1]:
       # print("ws -> ds를 dominate")
        dom.append(data_set[i])
        print("\n")
    else:
        #print("ds <> ws incomparable")
        incomparable.append(data_set[i])

        print("\n")

print(dom)
print("\n")
print(incomparable)
#print(data_set[0][1])
'''