
n=int(input("provide number to find sum of number: "))

def fact(n):
 sum=0

 for i in range(1, n+1):
    sum=i+sum
 return sum

    
sum=fact(n)
print(sum)



n = int(input("Provide number to find sum of numbers: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(sum)
