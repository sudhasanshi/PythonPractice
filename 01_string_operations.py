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
#it will split and stores in list format
sentence="hello All good!"
print(sentence.split()) #['hello', 'All', 'good!']
#it will split first one 
print(sentence.split(" ", 1)) #['hello', 'All good!']
#reverse split
print(sentence.rsplit(" ", 1))#['hello All', 'good!']

Basic build-in methods:
1.	lower(): It is used to convert string into lowercase
var = “Hello.World”)
var1 = var.lower()
print(var1)
2.	upper(): Used to convert string into uppercase
var = “Hello.World”)
print(var.upper())
3.	startswith(): used to check whether string is starts with pattern
var = “Hello.World”)
if var.startswith(“He”):
	print(“starts with pattern”)
else:
	print(“starts with different pattern”)
4.	endswith(): used to check whether string ends with specific pattern or not
5.	var = “Hello.World”)
if var.endswith(“He”):
	print(“ends with pattern”)
else:
	print(“sends with different pattern”)
6.	split(): used to split the string based on delimiter
var = “hello.wor.ld”
val, val1, val2 = var.split(‘.’)
above string is divided into 3 parts “hello”, “wor”, “ld”
val, val1= var.split(‘.’, 1)
above is splitted only one time since in function, 1 is passed. (Hello, wor.ld)
val, val1 = var.rsplit(‘.’, 1)
splitted from reverse order (Hello.wor, ld)
7.	replace: Used to replace the one character by another character
var = “hello.wor.ld”
var1 – var.replace(‘.’, ’/’)
print(var1) ------- Hello/wor/ld
