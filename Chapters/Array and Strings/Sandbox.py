#   Information of Array and Strings
# print("Info of Arrays and Strings: ")

# stri = " man , follow: something"
# str1 = stri.replace(" ","", -1)
# print(str1)

print("hello"   "1245")

# # Hash Maps / Dictionaries
# def hash():
#     t = 8
#     nums = [1,3,5,7,10]
#     map = {}
#     for index, n in enumerate(nums):
#         s = t-n
#         print( n , s ,index)
#         print(map)
#         print(s in map)
#         if s in map == True:
#             print("found it")
#         else:
#             print("not found")
#             map[n] = index
            
#     return

  

        
# def spaces(str):
#     array = []
#     for n in str:
#         if n == ' ':
#             print("space")
#         else:
#             print("char")
#             array.append(n)
            
#     print(array)
            
# # spaces("Hello Wolrd")

# def removeSpaces(str):
#     result = []
#     for index , n in enumerate(str):
#         # Probably create a list 
#         if n == ' ':
#             pass


# # removeSpaces("Hello Wolrd")


# # # Chat GPT:
# # class Solution:
# #     def permute(self, s: str):
# #         def backtrack(current):
# #             if not current:
# #                 result.append(s)
# #             else:
# #                 for char in s:
# #                     if char not in current:
# #                         backtrack(current + char)

# #         result = []
# #         backtrack("")
# #         return result

# # # Example usage
# # solution = Solution()
# # input_string = "abc"
# # permutations_array = solution.permute(input_string)
# # print(permutations_array)
            

# # Permutations:
# # Attempt 4
# array = [1,2,3]
# def permutations(array):
#     result = []
#     result.append(array)
#     print(f"{result} testings")
#     rec(array, result)
#     return result


# def rec(available, result):
#     # Check base case:
#     if len(available) == 2:
#         switched = switch(available)
#         #return store the switched version on result
#         result.append(switched)
#         return
    
    
#     # traverse
#     for n in available:
#         result.append(n)
#         temp_pointer = n
#         # add the pointer in result
#         available.remove(n)
#         rec(available, result)
#         available.append(temp_pointer)
        
    
#     return

# def switch(available):
#     tempSwitch = available
#     temp = tempSwitch[0]
#     tempSwitch[0] = tempSwitch[1]
#     tempSwitch[1] = temp
#     return tempSwitch



# # print(permutations(array))



# # Permutations attepmt 5:
# a = [1,2,3,4]

# def permute(nums):
#     #base case
#     if len(nums) == 1:
#         return [nums]
    
#     result = []
    
    
#     #traverse
#     for n in nums:
#         temp = [n]
#         copy = nums.copy()
#         copy.remove(n)
#         perm =permute(copy)

#         for p in perm: 
#             result.append(temp + p)
            
#     return result


# print(permute(a))



# Python Practice
# def payment():
#     hours = int(input("hours: "))
#     rate = float(input("rate : $"))
#     payment = hours*rate
#     print(f"payment is: ${payment}")
    
# payment()


# input  is in inches
# returns miles, feet, inches

# 1 mile = 5280 ft
# 1 ft = 12 in


# inches_per_foot = 12
# feet_per_mile =  5280
# distance_inches =   float(input("Enter distance inches: "))

# miles = distance_inches // (inches_per_foot * feet_per_mile)
# remaining_inches = distance_inches % (inches_per_foot * feet_per_mile)
# feet = remaining_inches // inches_per_foot
# inches = remaining_inches % inches_per_foot

# print(f"miles: {miles},feet: {feet},inches: {inches}")



# def inches_to_miles_feet_inches(distance_inches):
#     # Constants
#     INCHES_IN_A_FOOT = 12
#     FEET_IN_A_MILE = 5280

#     # Calculate miles, feet, and remaining inches
#     miles = distance_inches // (INCHES_IN_A_FOOT * FEET_IN_A_MILE)
#     remaining_inches = distance_inches % (INCHES_IN_A_FOOT * FEET_IN_A_MILE)
#     feet = remaining_inches // INCHES_IN_A_FOOT
#     inches = remaining_inches % INCHES_IN_A_FOOT

#     return miles, feet, inches

# # Get input from the user
# distance_inches = float(input("Enter distance in inches: "))

# # # Calculate and display the result
# # miles, feet, inches = inches_to_miles_feet_inches(distance_inches)
# # print(f"{distance_inches} inches is equal to {miles} miles, {feet} feet, and {inches} inches.")

# v=float(input("price? $"))
# c=input("color? ")
# if v<=25:
#   if c=="red":
#     print("buy")
#   elif c=="blue":
#     print("buy")
#   elif 5<v<15:
#     if (c=="white"):
#         print("buy")
#   elif v<=5:
#     print("buy") 
# else:
#   print("no buy")



# amount = 13.54

# dollar = 13.54 // 1       = $13
# amount = amount - 13    (13.54 - 13) = .54
# quarters = .54 // .25   -> 2
#amount = amount - .25*quarters ->    .54 - (.25*2)


lst = []
print(lst)