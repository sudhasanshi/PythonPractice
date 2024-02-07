num=int(input("enter number to check prime or not?)
for i in range(2, num):
    if num%i == 0:
        print("prime")
        break
    else:
        print("not prime")
