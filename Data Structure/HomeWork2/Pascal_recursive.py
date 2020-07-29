from time import time
import timeit

def pascal(n, k):  # note no dependencies on any of the prior code
    if k in (0, n):
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

def PA_r(c):
    for row in range(c):
        for k in range(row + 1):
            #print(pascal(row, k), end=' ', flush=True) 
            pascal(row, k)
        #print()
def PA_r_d(c):
    for row in range(c):
        for k in range(row + 1):
            print(pascal(row, k), end=' ', flush=True) 
        print()
        
#PA_r_d(6)