# Concepts Learned (Make Mistakes More Often to Improve)

#Print String and Integer together use f"string {int}"
def printStringInt():
    print(f"age: {22}")


# Hashmap
map = {}

# 1) For loop -> enumerate(map) get the index , keys
for index, number in enumerate(map):
    pass
# 2) adding to hashmap in a for loop be aware if you adding the index or the number first
index = 1
number = 22
map[index] = number

# How to get the keys and the val
class Hashmaps():

    def getKeys(map,val): #O(n)
        #Getting the key from the values is not a good stratrgy
        for key , value in map.items(): # items() 
            #print (key, value)
            if val == value:
                print(key)
        
        pass
    def getVals(map,key): #O(1)
        #This works instantly O(1)
        print(map[key])
        
    def getFunction(map,key):
        # to get the boolean use -> key in map
        
        #option 1
        if key in map:
            print(True)
        else:
            print(False)
            
        #option 2
        print(key in map)
#---------------------
Hashmap = {
    1:"First",
    2:"Second",
    3:"Third"
}
# Hashmaps.getKeys(Hashmap,"First")
# Hashmaps.getVals(Hashmap,2)
Hashmaps.getFunction(Hashmap,3)


#--------------------