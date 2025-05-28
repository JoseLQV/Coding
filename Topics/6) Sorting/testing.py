def quickSelect(arr, k):
    # Def divide
    def divide(left, right):
        # Base Case
        if left >= right:
            return arr[left]
        
        # Call Pivoting
        piv = pivoting(left, right)
        
        # Left Right 
        if piv == k: 
            return arr[piv]
        elif piv < k:
            return divide(piv+1, right)
        else:
            return divide(left, piv-1)
    
    # Def pivoting
    def pivoting(left, right):
        # Choose Pivot
        pivot = arr[right]
        swap_index = left
        
        # Traverse
        for curr in  range(left, right):
            # swap
            if arr[curr] < pivot:
                arr[curr], arr[left] = arr[left], arr[curr]
                swap_index += 1
            
        # Last Swap
        arr[swap_index] , arr[curr] = arr[curr], arr[swap_index]
        
        return swap_index
    
    return divide(0,len(arr)- 1)
    

print(quickSelect([4, 2, 6, 1, 5, 3], 2))
# Output: [1, 2, 3, 4, 5, 6]

