
n=int(input("provide number to find fact: "))

def fact(n):
 a=1

 for i in range(1, n+1):
    a=a*i
 return a

    
a=fact(n)
print(a)
