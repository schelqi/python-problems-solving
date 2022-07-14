import numpy

dimensions = input().strip().split()

#First array rows
N = int(dimensions[0])
#Second array rows
M = int(dimensions[1])
#Column
P = int(dimensions[2])

list_1 = list()
list_2 = list()

for i in range(N):
    row = list(map(int, input().strip().split()))
    list_1.append(row[0:P])

for i in range(M):
    row = list(map(int, input().strip().split()))
    list_2.append(row[0:P])


array_1 = numpy.array(list_1)
array_2 = numpy.array(list_2)


result = numpy.concatenate((array_1, array_2))

print(result)
