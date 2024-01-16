# 1.4 Palindromw Permutations: pg 91 -> pg 196
# Given a string , write a function to check if it is a permutation of a palindrome
# A palindrome is a word or phrase that is the same fowards and backwards.
# Permutations is the reareangements of letters. The palindrome does not need to be limited 
# to just dictionary words.

#Example:
#Input : Tact Coa
#Output : True (permutations: "taco cat", "atco cta", ect..)
# Hints : 106,121,134,136 



#-----------------------------------------------------------------------------------
# Attempt 2:

#Description get all permutations that also are palindrome
# Palindrome (word backwards or fowards)
# Permutations (rearrange letters)

#Conditions:
# Given a string
# Return all permutations that are palindrome and the boolean if found 
# Dont have to be in the dictionary

# Samples:
# Nulls and spaces or 1 letter
# output: True [permutations : "return input"]

#Input : Tact Coa
#Output : True (permutations: "taco cat", "atco cta", ect..)


#Brute force                                            
# Check ( exceptions )
#                                                  a         available (b,c,d)  
#                                                  b         (c,d)
#                                                  c         (d)
#                                                  d         ()    store(abcd)
#                                                           

    

#-----------------------------------------------------------------------------------
# Attempt 1:

# Description : check if is a permutation of a palindrome
# Palindrome: word same foward or backwards (if cut in half it has to have the same letters count left side and right side)
# Permutations: rearangements of letters (Length of characters must be the same)

#Conditions: 
# Given a String
# Palindrome not restricted by dictionary words
# Return Bolean and (all permutations that are palindrome)
# Space must stay in the same spot 

#Samples:
# ""  : True
# " " : True
# "taco tac"  True (permutations: "taco cat", "atco cta", ect..)
# "palind rome" False


#Brute Force: 
# Check(if empty or only a space)


# Info on Permutations
# How to solve for permutations
# get all permutations
# Function of all Permutation:
 
# Info on palindromes
# How to solve for palindromes 
# Function for Palindrome:

# Verify (permutation is a palindrome) 
# Store the palindrome and keep going

class PP():
    
    def PaliPerm(str):
        #CHECK (Exceptions)
        Result = []
        if str == None:
            return (f"{True} + (permutation: {Result})")
        if str == ' ' :
            Result.append(str)
            return (f"{True} + (permutation: {Result})")
        
        # Solve the problem of the spaces for the permutations (Fixed Space)
        
        fix_spaces = []
        for index , letter in enumerate(str):
            if letter == ' ':
                # Save the spaces of the string to hard code it in the result
                fix_spaces.append(index)
                # remove all the spaces from the string
                
                 
        
        
        # Call the Function for allPermutations:
        # add back the spaces to the corresponding spot
        
    
    def all_Permutations(nums): 
        result = ""
        
        #Base Case
        if(len(nums) == 1):
            return [nums.copy]
        
        for i in range(len(nums)):
            n = nums.pop()
            perms = allPermutations(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
            
        
        return result
            
        
        
            
            
    
    def palindromeCheck(str): 
        # Traverse the string with two pointer start and end until they meet in the same index
        # Return Boolean
        pass

