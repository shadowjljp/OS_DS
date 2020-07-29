def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 
def heapify(arr, n, i): 
                min = i  # Initialize smallest as root 
                l = 2 * i + 1     # left = 2*i + 1 
                r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # smaller than root 
                if l < n and arr[i] > arr[l]: 
                        min = l 
  
    # See if right child of root exists and is 
    # smaller than root 
                if r < n and arr[min] > arr[r]: 
                        min = r 
  
    # Change root, if needed 
                if min != i: 
                        arr[i],arr[min] = arr[min],arr[i]  # swap 
  
        # Heapify the root. 
                        heapify(arr, n, min)   
# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra 