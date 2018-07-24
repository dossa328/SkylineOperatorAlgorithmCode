# data set 만들기 [가격 , 해변으로부터의 거리]
data_set = [[45, 90], [35, 92], [43, 90], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]
# 크기가 3인 window set 만들기
window_set = [i for i in range(3)]
# 크기가 ? 인 temp set 만들기
T_TemporaryFile = []
# main memory; a set of d-dimensional points
S_MainMemory = []
# output of the Skyline operation; a set of d-dimensional points
M_InputSkyline = []
# input of the Skyline operation; a set of d-dimensional points
R_OutputSkyline = []

TImeStamp = 0
CountIn = 0
CountOut = 0
# while not EOF(M) do begin
for p_FirstData in data_set:
    # 각 S에 들어있는 p 마다 실행함
    for j in S_MainMemory:

        R_OutputSkyline.append(dataOut)

    p_FirstData.append(CountOut)
    CountIn = CountIn+1

    for q_SecondData in S_MainMemory:
        if p_FirstData == q_SecondData:
            break
        # p가 q에 의해 dominated 되면 release(p) and break
        # p가 q를 dominate 하면 release(q)
    # main memory 가 3이 아니라면 실행
    if not len(S_MainMemory) >= 3:
        # temp 에 p 넣기
        T_TemporaryFile.append(p_FirstData)
        # CountOut +1
        CountOut = CountOut + 1
    # EOF일때. 마지막으로 받은데이터가 data_set의 마지막요소와 같을때
    if q_SecondData == data_set[-1]
        # 메인메모리에다가 Temp 를 넣고
        M_InputSkyline.append(T_TemporaryFile)
        # Temp 비우기
        T_TemporaryFile = []
