
n=int(input("provide number to find fibo: "))

def fibo(n):
 a=0
 b=1
 print(f"{a}\n{b}")

 for i in range(2, n):
  fibo=a+b
  a=b
  b=fibo
  print(fibo)

    
fibo(n)
