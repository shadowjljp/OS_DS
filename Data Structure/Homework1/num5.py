from builtins import int

def square_root(num,guessCount=20):
    try:
        guessNum = float(num)
        for i in range (guessCount):
            num = 0.5*(num + guessNum/num) 
            
    except:
            print("Error: wrong format,please input an integer or float")
    
    return num

print(square_root(10))