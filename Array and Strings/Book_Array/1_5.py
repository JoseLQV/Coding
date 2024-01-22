# One Away: pg 91 -> pg196
# There are three types of edits that can be performed
# on strings: insert a character, remove a character, or replace a character. Given two strings, 
# write a function to check if they are one edit (or zero edits) away.

#Example:
#pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bake -> false
#Hints: #23,#97,#130

#-----------------------------------------------------------------
# Attempt 1:

# Description :
#  Boolean Function that check if the string was edited : insert,remove,replace or none 

#Conditions
#input: two string
#output: boolean
#can only edit the string once
#insert,remove,replace return true
# if none edits returns ?? (challenge False)

#Concept:

# take the string and the edited one
# create 3 functions: insert, remove, replace

# function that checks all of the following edits to see if its been edited
# insert:       
# compare = len(edited) - (len(not)
# if (compare) <= 0  or (compare) > 1: return false
# else: return true

# remove:       5-4
# compare = len(not) - len(edited)
# if compare == 1 return true
#else return false

#replace:
# compare = len(not) - edited
# if compare != 0: return false
# traverse through both strings check if one edited is changed 
# if changed once return true 
# else return False











