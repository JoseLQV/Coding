# String Compression: pg -> 91 , pg ->201

# Implement a method to perform basic string compression using the counts of repeated characters. For Example, 
# the string aabccccaaa would become a2b1c5a3.
# if the "compressed" string would not become smaller than the original string,
# your method should return the original string. You can assume the string has only 
# uppercase and lowercase letters(a-z). 

#hints #92, #110


#----------------------------------------------------------------
# Attempt 1:

# Description : return the compressed version of the string
# count the repeated chars

# Conditions:
# given a string
# count repeated chars 
#len of  compressed > string return string
# if len string <= 1 return string


# example:


# aabcccaaa -> a2b1c3a3




def OneAway(word):
    if len(word) <= 1:
        return word
    
    result = word[0]
    count = 1
    
    #traverse 
    i = 0
    j = i+1
    
    while(j < len(word)):
        if word[i] == word[j]:# repeated
            count += 1
        else: # not repeated
            result += str(count)
            count = 0 # reset
            result += word[j]
        
        i += 1.;'';''';'''
        j += 1
        
    
    return result

print(OneAway("aabcccaaaa"))
        
        
            
            
            
    
    
    
    



