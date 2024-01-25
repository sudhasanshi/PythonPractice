var="sudha"
age=24
id=100
print(f"my name is {var} and my age is {age} and id is {id}")
mylist=[10, "sudha", 10.0]
print(mylist)
print(mylist[1])
print(mylist[2])
mylist.append("hello")
print(mylist)
mylist.pop()
print(mylist)
var=["one", "two"]
var.extend(mylist)
print(var)
mylist.extend(var)
print(mylist)
count=len(mylist)
print(count)
