# IS UNIQUE  pg 90 -> pg 192
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures??
# hints: #44, # 117, #132

#---------------------------------------------------------------------------------
# Description:
#    Use one of the data structues ( hashmaps or arraylist  ) to solve the problem
#    Algorithm that Checks for a true or false ( if string has all unique characters )
#   Solution is a boolean

# True for unique
# False for duplicate

# Conditions :
#   Use only hashmaps or Arraylists
#   Info is in string format
#   Return boolean
#   string.size() > 128 return false 

# Does it has to be only int?
# Characters that are lower case and upper counts as one?
# Are there any upper cases or special signs 

# Exceptions and Samples:
#   null
#   44, 117, 132
#   ABC
#   aba

# Brute Force:  HASHMAP
#   Check (null) return True and len > 128 return false
#   Traverse string( store in a map)        -> O(n)
#       exist (return False)
#       store it
#   Return True

#--------------------------------------------------------
def solution(str):
    #Check:
    if len(str) > 128: return False
    if str == None: return True
    
    hashmap = {}
    # Traverse
    for letter in str:          
        if hashmap.get(letter) == 'exist':
            return False
        else:
            hashmap[letter] = 'exist'
    return True


test = solution("")
print(test)

    


