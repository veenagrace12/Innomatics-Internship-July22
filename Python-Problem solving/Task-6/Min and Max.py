import numpy

n, m = list(map(int, input().split()))
lst = numpy.array([list(map(int, input().split())) for _ in range(n)])
min_output = numpy.min(lst, axis=1)
print(numpy.max(min_output))




