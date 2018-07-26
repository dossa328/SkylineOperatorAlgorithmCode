'''
M_InputSkyline = [[39, 15], [47, 41], [82, 46], [51, 34], [65, 83], [98, 92], [75, 75], [60, 26], [22, 17], [15, 42],
                  [18, 14], [14, 32], [11, 36], [40, 90], [49, 91], [30, 35], [93, 15], [35, 89], [35, 62], [49, 20],
                  [25, 42], [89, 89], [84, 30], [79, 96], [98, 54], [13, 50], [17, 93], [83, 21], [96, 55], [45, 51],
                  [1, 56], [7, 5], [1, 84], [25, 9], [6, 95]]
'''
# data set 만들기 [가격 , 해변으로부터의 거리]

# 크기가 ? 인 temp set 만들기
T_TemporaryFile = []
# main memory; a set of d-dimensional points
S_MainMemory = []
# output of the Skyline operation; a set of d-dimensional points

M_InputSkyline = [[45, 90], [35, 92], [43, 90], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
#M_InputSkyline = [[1, 8], [2, 7], [3, 6], [1.5, 6]]
# input of the Skyline operation; a set of d-dimensional points
R_OutputSkyline = []
skyline = []
CountIn = 0
CountOut = 0
limit = 3
leng = 0


def dominated(looser, winner):
    dim = len(looser[0])

    # as good or better in all dimensions
    for i in range(dim):
        if winner[0][i] > looser[0][i]:
            return False

    # better in at least one dimension
    for i in range(dim):
        if winner[0][i] < looser[0][i]:
            return True

    return False


# while not EOF(M) do begin
while True:
    p_FirstData1 = []
    if M_InputSkyline:
        # 각 S에 들어있는 p 마다 실행함

        leng = len(S_MainMemory)
        removeElem = []

        for i in range(leng):
            if S_MainMemory[i][1] == CountIn:
                R_OutputSkyline.append(S_MainMemory[i][0])
                removeElem.append(S_MainMemory[i])

        for elem in removeElem:
            S_MainMemory.remove(elem)

        # load(M,p)
        p_FirstData1.append(M_InputSkyline[0])
        M_InputSkyline.remove(M_InputSkyline[0])
        p_FirstData1.append(CountOut)
        S_MainMemory.append(p_FirstData1)
        CountIn = CountIn + 1

        for q_SecondData in S_MainMemory:
            if p_FirstData1 == q_SecondData:
                pass
            else:
                # p가 q에 의해 dominated 되면 release(p) and break
                if dominated(p_FirstData1, q_SecondData):
                    S_MainMemory.remove(p_FirstData1)
                    p_FirstData1 = []
                    break
                # q가 p에 의해 dominated 되면 release(q)
                elif dominated(q_SecondData, p_FirstData1):
                    S_MainMemory.remove(q_SecondData)
                    q_SecondData = []

        # main memory 가 3이 아니라면 실행
        if not len(S_MainMemory) < limit:
            # temp 에 p 넣기
            T_TemporaryFile.append(p_FirstData1)
            S_MainMemory.remove(p_FirstData1)
            # CountOut +1
            CountOut = CountOut + 1
        # EOF일때. 마지막으로 받은데이터가 data_set의 마지막요소와 같을때
        if not M_InputSkyline:
            M_InputSkyline = []
            # Input memory에 Temp 를 넣고
            for i in range(len(T_TemporaryFile)):
                M_InputSkyline.append(T_TemporaryFile[i][0])
            # Temp 비우기
            T_TemporaryFile.clear()
            CountIn = 0
            CountOut = 0
    else:
        break
    # 각 S에 들어있는 p를 R에 대입하고 release p
for p_FirstData in S_MainMemory:
    R_OutputSkyline.append(p_FirstData[0])
# R 출력.

for p_FirstData in R_OutputSkyline:
    print(p_FirstData)
# 끝
