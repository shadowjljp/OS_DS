import math


def PA_d(n):
    for k in range(n) :
        for r in range(k+1):
            result = int((math.factorial(k)) / ((math.factorial(r)) * math.factorial(k - r))) 
            #print(result, end=' ', flush=True)
        #print()

def PA_d_d(n):
    for k in range(n) :
        for r in range(k+1):
            result = int((math.factorial(k)) / ((math.factorial(r)) * math.factorial(k - r))) 
            print(result, end=' ', flush=True)
        print()
        
PA_d_d(6)