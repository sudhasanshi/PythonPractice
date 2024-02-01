#range() is built-in method starts with 0
for i in range(10):
    print(i)
fruits=["apple", "orange", "banana", "grapes"]
for fruit in fruits:
    print(fruit)   

#using break condition to stop execution
for i in range(10):
    if i==5:
        break
    print(i) 
#using continue condition to skip that part and cotinue with execution
for i in range(10):
    if i==5:
        continue
    print(i)      
