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
            
