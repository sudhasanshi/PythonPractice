Fizzbuzz is a program that prints the numbers from 1 to n
1) for multiples of 3 it prints Fizz
2) for multiples of 5 it prints Buzz
3) and for multiples of both 3 and 5 it prints FizzBuzz

print("FizzBuzz Program")
my_list=[]
till_num=int(input("enter the number: "))
for num in range(1, till_num+1):
    result=""
    if num%3==0:
      result=result + "Fizz"
      if num%5==0:
         result=result+"Buzz"
    elif num%5==0:
       result=result+"Buzz" 
    else:
       result=num    
    my_list.append(result)

print(my_list)
    
