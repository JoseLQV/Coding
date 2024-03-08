
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


#------------------------------------------------------------------------------------------

# ATTEMPT 2:

# Description: Array of Int , find the elements index of the sum that = to target

# Conditions:
    # Array of int
    # array wont be empty
    # output any order
    # given target and array
    # only one solution

# Exceptions and samples:

    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    # Example 2:

    # Input: nums = [3,2,4], target = 6
    # Output: [1,2]
    # Example 3:

    # Input: nums = [3,3], target = 6
    # Output: [0,1]
    
    # Input: nums = [] , target = []
    #  Output: []

# Brute Force:     
    #Input: nums = [2,3,5,7,8,11,15], target = 13
    # Output: [0,1]
   
   #Check (none)
   #Traverse through array
    # If target - number found in hash return 
    # else: add to hash
   
   
def solution(nums,target): #O(n)
    #Check 
    if target == None or nums == None:
        return []
    
                #key -> val
    map = {} # number : index 
    #Traverse
    for index, number in enumerate(nums):
        diff = abs(target - number)
        
        # Found it
        if diff in map: 
            return [map[diff], index]
        
        #Not Found
        else:
            map[number] = index 
    
    return []
            
            

   
   
   
   
   
    

         




















#------------------------------------------------------------------------------
        # ATTEMPT 1
# Description: given array of int, two nums that sum to target ,  RETURN THE INDEX

# Conditions: 
#   RETURN THE INDEX
#   array of int (unsorted)
#   garanteed only one solution
#   not repeat same element
#   solution can be any order

# Exceptions and Samples:
#   if empty or null
#   [2,3,4,5,6] t = 9 : [4,5]
#   [3,2,11,2,44,7] t = 10 : [3,7]
#   [3,5,9]
                                                            #       i      j
# Brute Force:          O(N^2)                                    [2,3,4,5,6] t = 9 : [4,5]
#   CHECK ( EMPTY )  
#   Sort ( array )      -> O(n)
#   Traverse array ( i and j )  -> O(n^2)
#       Compare( target wuth sum ) 
#   Return Result
                                                            
#Brute force 2:         O(N)   HashMap                            [3,2,11,2,44,7] t = 10 : [3,7]
   
   #                                                               i  +    j
# Brute Force 3:    Binary search                                 [2,3,4,5,6] t = 9 : [4,5]
# Check (empty)
# Sort (array)   o(n)
# Traverse array 
#   if (sum > t) j--
#   if ( sum < t) i++
#   if i >= j return null
#   if (sum = t) Found It

# Return Result





class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #Check
        result = []
        if nums == None or target == None:
            return result
        
         # [3,2,11,2,44,7] t = 10 : [3,7]
        #Sort
        sorted = nums
        sorted.sort()
        
        #Traverse Array
        left = 0
        right = len(sorted)-1
        sum = sorted[left] + sorted[right]
        while( left < right):
            if (sum == target):
                result = [left,right]
                break
            elif sum > target:
                right -=1
            else :
                left += 1
            
            sum = sorted[left] + sorted[right]    

        # correcting indexes
        index_left = nums[sorted[left]]
        index_right = nums[sorted[right]]
    
        corrected_result = [index_left,index_right]
        return corrected_result
            
            
# Failed Attepmt 1 Because didnt observe that you have to give the index from the main list not the result
# and changing the values in a sorted array changes its index 

  
