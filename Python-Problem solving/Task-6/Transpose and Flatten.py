import numpy
n,m=map(int,input().split())

lst=[list(map(int,input().split())) for i in range(n)]
nmpy_arr=numpy.array(lst)

print(numpy.transpose(nmpy_arr))
print(nmpy_arr.flatten())



