M_InputSkyline = [[45, 90], [35, 92], [43, 90], [49, 8], [4, 61], [10, 22], [48, 51], [92, 5], [10, 40]]

Partition1 = []
Partition2 = []

m_pivot_sum =0

def skyline_basic(M, dimension):
    if len(M) == 1:
        return M

    for i in range(len(M_InputSkyline)):
        pivot_sum = m_pivot_sum + M_InputSkyline[i][0]

    pivot = m_pivot_sum / len(M_InputSkyline)
