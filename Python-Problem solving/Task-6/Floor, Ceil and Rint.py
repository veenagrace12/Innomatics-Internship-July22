import numpy

numpy.set_printoptions(legacy='1.13')

A = numpy.array(input().split(),float)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
