# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
#----------------------------------------------------------------------------------
# Attempt 1:

# Description: Return all the permutation of the given array of characters

#Conditions:
# Input array (Integer)
# Output : 2D array
# Nums in array are Unique
# output : Any Order

#Exceptions:
# it wont be null
# array of unique characters


# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]

#Brute Force: 
# Formula?
# Nested For loops?

    # Queues? 
    
# I can probably rotate while mantaining one fixed


#                   _      _      _
                #  _ _    _ _     _ _
                #_    _   _  _    _  _
                
# Recursion:
# Go through the problem and keep reducing the options


def Perm(nums):
    matrix = {}
    
    pass
def recursion(available_nums, matrix, curr_path):
    available_nums= []
    
    pass