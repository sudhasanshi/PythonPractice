
n=int(input("provide number to find sum of number: "))

def fact(n):
 sum=0

 for i in range(1, n+1):
    sum=i+sum
 return sum

    
sum=fact(n)
print(sum)
