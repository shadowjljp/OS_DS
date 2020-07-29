import timeit
from HomeWork2.Pascal_recursive import *
from HomeWork2.Pascal_array import *
from HomeWork2.Pascal_nonarray import *

while (1):
    n= input("input the degree n : ")
#PA_r(6)
#PA_n(6)
#PA_d(6)

    
    t1 = timeit.timeit(stmt="PA_r("+n+")", setup="from  HomeWork2.Pascal_recursive import PA_r", number=1)
    print("Recursion execution time: {}".format(t1)) 
    
    t2 = timeit.timeit(stmt="PA_n("+n+")", setup="from  HomeWork2.Pascal_array import PA_n", number=1)
    print("Non-Recursion execution time: {} ".format(t2))
    
    t3 = timeit.timeit(stmt="PA_d("+n+")", setup="from  HomeWork2.Pascal_nonarray import PA_d", number=1)
    print("Direct Computation execution time: {} ".format(t3))             
