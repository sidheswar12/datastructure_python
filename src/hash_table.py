
#TODO: dictionary 
item1 = dict({"key3": "three","key1": 1, "key2": 4, "key4": 9})
print(item1)

# Acces value through key
print(item1["key3"])

item2 = {} # Empty dictionary
# Assigne key value to dictionary
item2["key1"] = 1
item2["key2"] = 2
item2["key3"] = 3

print(item2)

# TODO Replace
item2["key2"] = "two"
print(item2)

# Traverse the hastable
for key, value in item1.items():
    print("Key:", key, "Value:", value)

