from HomeWork3.Stack import Stack

while(1):
    try:
        n=input("Please enter the number of bits for the Gray Code: ")
        n=int(n)
    
        list=[0,1]
        i=1
        s=Stack()   #stack is here
        
        
        while(i<n):
            i=i+1
#add elements into stack for using its FILO properties to achieve reflection
            for k in range(pow(2,i-1)): 
                s.push(list[k])
            
            for k in range(pow(2,i-1)):
                list[k]='0'+(str)(list[k])
        
#Take out the elements in stack to put them into list one by one to form the final answer  
            for k in range(pow(2,i-1)):
                list.append('1'+(str)(s.pop()))                          

        print(list)
    except:
        print("please enter a integer only")    
   
    




