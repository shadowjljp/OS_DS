import math
class Node:
        def __init__(self,name=None,key=None):
                self.left=None
                self.right=None
                self.name=name
                self.key=key
      

class Main:
        
        
        def __init__(self):
                self.root = None


        def HeapwithEntriesInserted(self):
                global newContent,NewContentNode
               # reader = open("Data Structure\HomeWork5\inFile.txt","r")
                #print(reader.read())
                with open("HomeWork5\inFile.txt","r") as f:
                        content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip().split() for x in content] 
        #        print("Whole contents are ",content)
                #print(content[0][0])

                
                HeapSize=len(content)
               

                #setting up root for insert later
                if self.root is None:
                        self.root=Node(content[0][1],content[0][0])

                #insert process     
                self._insert(self.root,content,HeapSize)
                
                #info about Heap size and the hightest priority
                self.heapinfo(HeapSize,highest)

                #pre-order traversal the Heap
                print("pre-order traversal: ")
                if self.root:
                        self.preorderTraversal(self.root) #preorder Traversal
                        
                else:
                        print("The root is empty")

                #remove process
                self.removeMin()
                self.removeMin()
                self.removeMin()
                self.removeMin()
                self.removeMin()


                newContent = []
                NewContentNode=[]
                newContent.append(35)
                newContent.append("resume")
                newContent.append(15)
                newContent.append("seocnd")
                newContent.append(20)
                newContent.append('fourth')
                #insert new content
                v1 = Node('resume',35)
                v2 = Node('seocnd',15)
                v3 = Node('fourth',20)
                NewContentNode.append(v1)
                NewContentNode.append(v2)
                NewContentNode.append(v3)
                self.Insert(v1)
                self.Insert(v2)
                self.Insert(v3)
                self.heapinfo(new_size,new_highest)

                
                #mini Heap adjustment
                self.downwardHeapify(self.root)
                self.remove()
                self.adj_Insert()
                
                #pre-order traversal the Heap
                print("pre-order traversal: ")
                if self.root:
                        self.preorderTraversal(self.root) #preorder Traversal
                        
                else:
                        print("The root is empty")
                
        def heapinfo(self,HeapSize1,highest1):
                print(str("Heap size = "+str(HeapSize1)+" The highest priority is "+str(highest1)))
        def adj_Insert(self):
                self.root = NewContentNode[0]
                self.root.left = NewContentNode[1]
                self.root.right = NewContentNode[2]

        def _insert(self,cur_node,content,HeapSize):
                global highest,list
                highest = int(content[0][0])
                list=[]
                list.append(cur_node)
                for i in range (1,HeapSize):   
                        if highest >int(content[i][0]):
                                highest=int(content[i][0])
                        l=2*i+1
                        r=2*i+2        
                        if(i%2==1):
                                
                                cur_node.left=Node(content[i][1],content[i][0])
                                list.append(cur_node.left)
                                cur_node.left.parent = cur_node
                              #  if(i>2 and cur_node.left) :
                               #         self._insert(cur_node.left,i)
                        elif (i%2==0):
                               
                                cur_node.right = Node(content[i][1],content[i][0])
                                list.append(cur_node.right)
                                cur_node.right.parent= cur_node
                                temp=int(i/2)
                                cur_node=list[temp]
                #print("list is here ", Node.key)
#                print ("list is here",[Node.key for Node in list])       

        def preorderTraversal(self, Node):
                
                res = []
                if Node:
                        res.append(Node.key)
                        res.append(Node.name)
                        if Node.left:
                                print("Node [",Node.key , Node.name,"]")
                        else:
                                print("Leaf [",Node.key , Node.name,"]") 
                        res = res + self.preorderTraversal(Node.left)
                        
                              
                        res = res + self.preorderTraversal(Node.right)
                return res

        def removeMin(self):
                if list:
                        length = len(list)
                        min=(list[0]).key
                        i_indicater=0
                

                        for i in range(1,length):
                                if min >(list[i]).key:
                                        min=(list[i]).key
                                        i_indicater=int(i)
                        list.pop(i_indicater)
                        if not list:
                                print("The heap is now empty")
                elif not list:
                         print("The heap is now empty and no entry can be removed")
                print("deleteMin")
        def remove(self):
                
                self.root.right=None
                self.root.left=None
                self.root=None
                        
                               
                
                         
                
        def Insert(self,Node):
                global new_size,new_highest
                
                
                new_size = len(NewContentNode)

                min = NewContentNode[0].key 
                tip = NewContentNode[0].key 
                if(min>NewContentNode[1].key):
                        min=NewContentNode[1].key
                if(min>NewContentNode[2].key):
                        min = NewContentNode[2].key
              
                new_highest = min
                
                self.root= NewContentNode[0]
                
                self.New_insert(self.root,new_size)

        def New_insert(self,cur_node,new_size):
             cur_node.left=NewContentNode[1]
             cur_node.right = NewContentNode[2]

        def downwardHeapify(self,Node):
                size=len(NewContentNode)
               
                for i in range(0,size):
                        l=(2*i+1)
                        r=(2*i+2)
                        if(l<=size and r <=size):
                                tip = int(NewContentNode[i].key)
                                min =tip
                                i_min=i
                                tipl=int(NewContentNode[l].key)
                                tipr = int(NewContentNode[r].key)
                                if(min>tipl):
                                        min = tipl
                                        i_min=l
                                if(min>tipr):
                                        min = tipr
                                        i_min=r
                                if(min != tip):
                                        NewContentNode[i_min],NewContentNode[i]=NewContentNode[i],NewContentNode[i_min] # exchange
       
        def upwardHeapify(self,Node):
                
                size=len(NewContentNode)
                for i in range (0,NewContentNode):
                        if(Node ==NewContentNode[i]):
                                tempSize = i 
                for i in range(tempSize,0,-tempSize/2):
                        tempi = math.floor(i)
                        if (NewContentNode[tempi]%2 ==1 and NewContentNode[tempi+1]):
                                nodeR = NewContentNode[tempi+1].key
                                nodeL = NewContentNode[tempi].key
                                nodeP = NewContentNode[math.floor(tempi/2)].key       #parent
                                indicater = math.floor(tempi/2)
                                min = nodeP
                                if(min>nodeR):
                                        min = nodeR
                                        indicater=tempi+1
                                if(min>nodeL):
                                        min = nodeL
                                        indicater=tempi
                                if(min!=nodeP):
                                       NewContentNode[math.floor(tempi/2)],NewContentNode[indicater] =NewContentNode[indicater],NewContentNode[math.floor(tempi/2)]
                        else:
                                nodeR = NewContentNode[tempi].key
                                nodeL = NewContentNode[tempi-1].key
                                nodeP = NewContentNode[math.floor(tempi/2)].key       #parent
                                indicater = math.floor(tempi/2)
                                min = nodeP
                                if(min>nodeR):
                                        min = nodeR
                                        indicater=tempi
                                if(min>nodeL):
                                        min = nodeL
                                        indicater=tempi-1
                                if(min!=nodeP):
                                       NewContentNode[math.floor(tempi/2)],NewContentNode[indicater] =NewContentNode[indicater],NewContentNode[math.floor(tempi/2)]                  
                       
       
        
T= Main()
T.HeapwithEntriesInserted()
                        
