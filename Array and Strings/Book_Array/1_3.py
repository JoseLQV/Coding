#1.3 URLify: pg 90 -> pg 194
# Write a method to replace all spaces in a string with %20. You can assume that the string 
#has sufficient space at the end to hold the additional characters, and that you are given 
# the "true" length of the string. (Note: if implementing in Java, Please use a character
# array so that you can perform this operation in place.)
#Example:
# Input: "Mr John Smith" , 13
# Output: "Mr%20John%20Smith"
#Hint: 53, 118

#--------------------------------------------------------------------------------------
# Attempt 1

#Description: replace all spaces with %20 in a string

#Conditions:
# Given string
# Given string length (including spaces) why is it given????
# replace spaces with %20


# Exception or Samples:

# Input: "Mr John Smith" , 13
# Output: "Mr%20John%20Smith"


#Input : "" , 0

#Input : " " , 1

# Brute Force:
#   Check (if null or only a space)
#   Traverse (array and find the spaces and replace them)
#   return (new string)


def Spaces(str,length): #O(n)
    #Check:
    newStr = ''
    if str == None:
        return newStr
    
    #Traverse
    for n in str:
        #replace
        if n == ' ':
            newStr += "%20"
        else:
            newStr += n
    return newStr

str = "Hello World"
print(Spaces(str,len(str)))


            
