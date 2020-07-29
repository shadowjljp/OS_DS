# n = int(input("please input an integer.\n"))
# m= int(input("please input another integer.\n"))



def is_bigger(n, m):  # function
        
        if type(n) is not int and type(m) is not int:  # Check parameters` type
            print('Both of your parameters are not integer!')
        elif type(n) is not int:
            print ('Your first parameter is not an integer!')
        elif type(m) is not int:
            print ('Your second parameter is not an integer!')
        elif n > m:                         #Comparison starts here.
            print ("{0} is bigger.".format(n))
        elif m > n:
            print (m, "is bigger.")
        elif n == m:
            print ('Both integer values are equal,no one is bigger.')

