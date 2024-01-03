#   Information of Array and Strings
print("Info of Arrays and Strings: ")



# Hash Maps / Dictionaries
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

  

        
        
        
        
        

# hash_map = {
#     2:"something",
#     3:"testing"
#     }
# hash_map[1] = "hello world"

# hash_map.get(1)


# print(hash_map.get(1))



# Array List / Lists

# String Builder

