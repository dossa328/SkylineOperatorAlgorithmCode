# data set 만들기 [가격 , 해변으로부터의 거리]
database = [[45, 90], [35, 92], [43, 90], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
# 크기가 3인 window set 만들기
window_set = [i for i in range(3)]
# 크기가 ? 인 temp set 만들기
T_TemporaryFile = []
# main memory; a set of d-dimensional points
S_MainMemory = []
# output of the Skyline operation; a set of d-dimensional points
#M_InputSkyline = [[45, 90], [35, 92], [43, 90], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
M_InputSkyline = [[1, 8], [2, 7], [3, 6], [1.5, 6]]
# input of the Skyline operation; a set of d-dimensional points
R_OutputSkyline = []
skyline = []
CountIn = 0
CountOut = 0


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
    q_SecondData1 = []
    if M_InputSkyline:
        # 각 S에 들어있는 p 마다 실행함
        for p_FirstData in S_MainMemory:
            if p_FirstData[1] == CountIn:
                R_OutputSkyline.append(p_FirstData)
                p_FirstData.clear()

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
                    p_FirstData1 = []
                    break
                # p가 q를 dominate 하면 release(q)
                elif not dominated(p_FirstData1, q_SecondData):
                    S_MainMemory.remove(q_SecondData)
                    q_SecondData = []

        # main memory 가 3이 아니라면 실행
        if not len(S_MainMemory) < 3:
            # temp 에 p 넣기
            T_TemporaryFile.append(p_FirstData1)
            S_MainMemory.remove(p_FirstData1)
            # CountOut +1
            CountOut = CountOut + 1
        # EOF일때. 마지막으로 받은데이터가 data_set의 마지막요소와 같을때
        if q_SecondData == database[-1]:
            # Input memory에 Temp 를 넣고
            M_InputSkyline.append(T_TemporaryFile)
            # Temp 비우기
            T_TemporaryFile.clear()
            CountIn = 0
            CountOut = 0
    else:
        break
    # 각 S에 들어있는 p를 R에 대입하고 release p
for p_FirstData in S_MainMemory:
    R_OutputSkyline.append(p_FirstData)
# R 출력.
print(R_OutputSkyline)
# 끝
