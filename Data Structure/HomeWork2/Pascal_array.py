import math


def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))


def PascalCalcution(rows):
    result = [] # need something to collect our results in
    for count in range(rows): # start at 0, up to but not including rows number.
        row = [] # need a row element to collect the row in
        for element in range(count + 1): 
            row.append(combination(count, element))
        result.append(row)
        # count += 1 # avoidable
    # Here we can print a result:
    return result

    
    #for row in range(len(result)):
def PA_n(c):
        for row in PascalCalcution(c):
            #print(row, end=' ', flush=True) HomeWork does not require to print them out.
            row
def PA_n_d(c):
        for row in PascalCalcution(c):
            print(row, end=' ', flush=True) 
#PA_n_d(6)