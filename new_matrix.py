import numpy, sys, time
import csv

"""
if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])
"""

N = [i for i in range(3,21)]
time_list = list()

for n in N:
    print(n)
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C
    
    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            #print("a",i,j,a[i,j])
            b[i, j] = j * n + i
            #print("b",i,j,b[i,j])
            c[i, j] = 0

    begin = time.time()
    print(begin)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i,j] += a[i,k] * b[k,j]

    end = time.time()
    print(end)
    exc_time = end - begin
    time_list.append(exc_time)
    print("time: %.6f sec" % exc_time)
    
    # Print C for debugging. Comment out the print before measuring the execution time.
    total = 0
    for i in range(n):
        for j in range(n):
            #print(i,j,c[i, j])
            total += c[i, j]
    # Print out the sum of all values in C.
    # This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
    print("sum: %.6f" % total)

with open('execution_time.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(time_list)
        
