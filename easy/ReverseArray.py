import numpy

def arrays(arr):  # arr is a list
    # complete this function
    # use numpy.array
    array = numpy.array(arr, float)
    reversed_array = array[::-1]
    return reversed_array

arr = input().strip().split(' ') #list
result = arrays(arr)
print(result)