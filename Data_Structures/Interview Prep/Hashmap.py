# ------- Creating Hashmap -----------
initialize_map = {} 

# Curly Braces
m = {"key" : "value", "key1" : "value1", "key3": "value3"}

# Dict() Contructor
m1 = dict([("key1", 1), ("key2", 2)])


# --------- Accessing Values -----------

# variable
value = m["key"]

# Modifying values and keys
m['key3'] = "Changed the value"

m["value1"] = "new key"

# Adding pairs
m["key4"] = "Added value"
m["key5"] = "testing"

#Removing pairs
r = m.pop("key5")
r1 = m.get("value")
print(r1)



# ------- Hashmap For loops --------

for key in m:
    print(key)

for value in m.values():
    print(value)

for key,value in m.items():
    print (key,value)




