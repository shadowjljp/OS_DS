import re
import string


#Determine whether the input is correct or not
while(1):
    id = input('Please input your personal ID: ')
    preRegularExpression = re.match(r'^[a-z]$',id[0],flags=0)
    RegularExpression = re.match(r'^[A-Z]\d{9}$',id,flags=0)
    if id=='exit()':
        break
    if not RegularExpression \
        or int(id[1]) > 2 or int(id[1]) < 1:
            print('Error: wrong format')
            if preRegularExpression:
                print('Error:The first letter must be uppercase!')
            continue
#     else:
#         print('right')
    firstLetter = list(string.ascii_uppercase[0:])  #first letters
    code = list(range(10,35))                   #letters match number
    locationNum = dict(zip(firstLetter,code))   #mapping them through dict
    
    numericID = list(str(locationNum[id[0]]))
    numericID.extend(list(id[1:]))
    sum = int(numericID[0])   #numeric the first letter from input
 
    
    #calculate the sum
    constant = 9
    for n in numericID[1:]:
        if constant ==0:
            constant=1
        sum +=int(n)*constant
        constant-=1
    

        
    if sum%10==0:
        print('ID is Valid')
    else:
        print('Error:ID is Invalid')
