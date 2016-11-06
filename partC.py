import numpy

filenameIs = raw_input("File path: ")
file = open(filenameIs, 'r')

def makematrix(filename):
    file.readline()
    siz = int (file.readline())
    matrix = numpy.matrix(numpy.zeros((siz,siz)))
    file.readline()
    file.readline()
    for line in file:
        indexes = line.split(' -- ')
        matrix[int(indexes[0]),int(indexes[1])] = 1
        matrix[int(indexes[1]),int(indexes[0])] = 1
    return matrix

def findpath(matrix, m):
    return matrix ** m #the value at i,j will be the number of paths from i to j of length m

print findpath(makematrix(file), 4)



