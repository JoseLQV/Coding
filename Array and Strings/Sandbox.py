#   Information of Array and Strings
print("Info of Arrays and Strings: ")



# Hash Maps / Dictionaries
def hash():
    t = 8
    nums = [1,3,5,7,10]
    map = {}
    for index, n in enumerate(nums):
        s = t-n
        print( n , s ,index)
        print(map)
        print(s in map)
        if s in map == True:
            print("found it")
        else:
            print("not found")
            map[n] = index
            
    return
  

        
def spaces(str):
    array = []
    for n in str:
        if n == ' ':
            print("space")
        else:
            print("char")
            array.append(n)
            
    print(array)
            
# spaces("Hello Wolrd")

def removeSpaces(str):
    result = []
    for index , n in enumerate(str):
        # Probably create a list 
        if n == ' ':
            pass


removeSpaces("Hello Wolrd")


# # Chat GPT:
# class Solution:
#     def permute(self, s: str):
#         def backtrack(current):
#             if not current:
#                 result.append(s)
#             else:
#                 for char in s:
#                     if char not in current:
#                         backtrack(current + char)

#         result = []
#         backtrack("")
#         return result

# # Example usage
# solution = Solution()
# input_string = "abc"
# permutations_array = solution.permute(input_string)
# print(permutations_array)
            

# Testing
array = [1,2,3,4]
def permutations(array):
    result = [[]]
    rec(array, result)
    return result


def rec(available, result):
    # Check base case:
    if len(available) == 1:
        switched = switch(available)
        #return store the switched version on result
        
    # traverse
    for n in available:
        temp_pointer = n
        # add the pointer in result
        available.remove(n)
        rec(available, result)
        available.append(temp_pointer)
        
    
    return result

def switch(available):
    tempSwitch = available
    temp = tempSwitch[0]
    tempSwitch[0] = tempSwitch[1]
    tempSwitch[1] = temp
    return tempSwitch



