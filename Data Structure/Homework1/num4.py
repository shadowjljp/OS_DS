import re


def selection_sort(A):
        OriList=list(map(int,A.split())) #turn A from String list to int list
        OriListTemp = OriList[:] #make a copy of OriList before it gets all pop() out

        sortedResult =[]  
        while(len(OriList)!=0):
            minIndex = OriList.index(min(OriList)) #retrieve the min index of the min value in the list
            sortedResult.append(OriList[minIndex]) #add the min value to the new list
            OriList.pop(minIndex)             #delete the min value and back to get another one
        print('The sorted array',OriListTemp,'is',sortedResult)


while(1):
    
    A = input('Please enter the numbers to be sorted and separate them by spaces: ')

    regExg = re.match(r'^\d+(?:\s+\d+)+$', A, flags=0)
    if A=='exit()':
        break
    if not regExg:
        print('Error:Wrong format')
    
    else:
#         print('correct')
        selection_sort(A)
