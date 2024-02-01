fruits=["apple", "orange", "banana"]
for fruit in fruits:
    print(fruit)
for index, fruit in enumerate(fruits):
    print(index, fruit)    
my_dict={"name": "sudha", "location": "BLR"}
for key in my_dict.keys():
    print(key)    
for value in my_dict.values():
    print(value)  
for key, value in my_dict.items():
    print(F"{key} : {value}")    
mydict={"name":["sudha","manju"], "class":["A", "B"], "location":"BLR" }
for key, value in mydict.items():
    print(key, value)
