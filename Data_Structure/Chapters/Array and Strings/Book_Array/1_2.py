#1.2 Check Permutations: pg 90 -> pg 193
# Given two strings, write a method to decide if one is a permutation of the other
# Hints: 1,84,122,131

# Description:
#Check if is a combination of the other
# Permutation of abc =  (abc), (acb), (bac)

#Conditions:
# Check two strings
# It can be NULL
# Output is a boolean
# Lower Case and Upper Case sensitive??

#Exceptions and Samples:
# Nulls (both) (one)
# abc -> abc, acb , bac , bca , cab, cba (P = 6)
# 84 -> 84, 48 (P = 2)

#Brute Force1: Get all the combinations and then check the second string , Time complexity would be horrible

#Brute Force2: Hashmap, 
# Len diff ( return false)
# Store (string into hashmap)
# Check (second string if the same amount of characters)


#-----------------------------------------------------------------------------
# Attempt 1: 

def Permutations(str1, str2): #O(N+M) = O(N)
    #diff
    if len(str1) != len(str2):
        return False
    #store:
    map = {}
    for c in str1:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1
            
    #check:
    for c in str2:
        if c in map:
            map[c] -= 1
        else:
            return False
    
    return True


