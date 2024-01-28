#to uppercase
var="sudha"
print(var.upper())
#to lowercase
print(var.lower())
#length of string
print(len(var))
#appending string
print("sudha" + " "+ "sanshi")
value=" life/ is /beautifull "
#spliting words
print(value.split("/"))
print(value)
#striping
value="    life is beautifull    "
striped_value=value.strip( )
print(striped_value)
#replacing string value
print(value.replace("life","flower"))
#to check string start with specific pattern and it will return true or false
value="hello"
print(value.startswith("h"))
#to join 
print(value.join('good'))
value="Name"
print(value.startswith("Na"))
print(value.endswith("e"))
print(value.lower().startswith("Na"))
print(value.lower().startswith("na"))
