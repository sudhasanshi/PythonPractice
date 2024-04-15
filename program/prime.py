num=int(input("enter number to check prime or not?"))
for i in range(2, num):
    if num%i == 0:
        print("prime")
        break
    else:
        print("not prime")



num = int(input("Enter a number to check prime or not: "))
i = 2

while i * i <= num:
    if num % i == 0:
        print(f"{num} is not prime.")
        break
    i += 1
else:
    print(f"{num} is prime.")
