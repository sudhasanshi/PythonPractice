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
