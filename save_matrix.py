import numpy as np
columns = 15
rows = 15
matrix = []
start = 1
end = 100
value = start
step = (end - start) / (rows * columns -1)
dataList = range(1,100)
for x in range(rows):
    listrow = []
    for i in range(columns):
        listrow.append(value)
        value += step
    matrix.append(listrow)
matrix = np.array(matrix)

np.savetxt("matrix.txt", matrix)