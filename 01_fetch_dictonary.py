sub= {"birds": ["sparrow", "kingfisher", "parrot", "macaw", "hummingbird"], "types": {"intigers": [1, 2, 3, 4, 5],
    "floats": None, "alphabets": {"vowels": ['a', 'e', 'i', 'o', 'u'], "consonants": "bcdfghjklmnpqrstvwxyz"}},
      "mydict" :{"avengers": ["hulk", "antman", "spiderman"], "xmen": ["raven", "wovelirin"]}}
for s in sub:
    print(s) # it will print all the keys of dictionary
for index, keys in enumerate(sub):
    print(keys,index) # it will print keys and index values
for key in sub.keys():
    print(key) # it will print all keys one by one
for value in sub.values():
    print(value) # it will print all values 
for key, value in sub.items():
    print(key,value)# it will print both all keys and values

mydict={}
print("my empty dictionary is ", mydict)
mydict={"name": "abc", "id": 1}
print("my dictionary values", mydict)
print(mydict["name"])
print(mydict["id"])
mydict={"name": ["abc", "xyz"], "id": 1}
print(mydict)
print(mydict["name"][1])
mydict={"name": ["abc", "xyz"], "clases": ["A", "B", "C"], "details":{"age": 23, "places": ["BLR", "BGK"], "phone_no": 8787}}
print(mydict["details"]["places"][1])
print(mydict["details"]["phone_no"])
mydict={"Resource":"arn:aws:iam::123456789012:user/*"}
print(mydict["Resource"])
