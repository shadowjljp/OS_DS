import re

def get_num(fraction):
    fractionList = fraction.split('/', 1) #separate numerator and denominator
    
    return fractionList[1]

def get_den(fraction):
    fractionList = fraction.split('/',1)
    return fractionList[0]


while (1):
    fraction = input("please input a fraction: ")
    if fraction=='exit()':
        break
    regularExpression= re.match(r'[1-9][0-9]*\/[1-9][0-9]*',fraction,flags=0)
    if regularExpression:
        print("The denominator is :\n",get_den(fraction))
        print("The numerator is :\n",get_num(fraction))
    else:
        print("Error:Wrong format,please enter a fraction.")
    continue