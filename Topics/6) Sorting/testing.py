def quickSort(arr):
    
    # Def sort
    def sort(left_index,right_index):
        # Base Case
        if left_index >= right_index:
            return 
        
        # Call Partition 
        part = partition(left_index,right_index)
        
        # Left Right Call
        sort(left_index , part-1)
        sort(part+1 , right_index)
    
    
    # Def partition
    def partition(left_index,right_index):
        # Choose Pivot
        pivot =  arr[right_index]     
        
         # Traverse swap
        for curr_index in range(left_index, right_index ):
            if arr[curr_index] < pivot :
                
                arr[left_index], arr[curr_index] = arr[curr_index] , arr[left_index]
                left_index += 1
        
        
        # Swap Left Right
        arr[left_index] , arr[right_index] = arr[right_index] , arr[left_index] 
        
        # Return Left
        return left_index
        
        
    
    # Call sort
    sort(0,len(arr)- 1)
    return arr
        
            

print(quickSort([4, 2, 6, 1, 5, 3]))
# Output: [1, 2, 3, 4, 5, 6]
      
            
                
                
                
        
    
   