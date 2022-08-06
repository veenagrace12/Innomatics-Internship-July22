import numpy
numpy.set_printoptions(legacy="1.13")

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
nmpy_sum=numpy.sum(A, axis=0)
print(numpy.prod(nmpy_sum))


