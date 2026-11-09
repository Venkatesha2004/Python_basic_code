print("enter a number")
n=int(input())
if n<2:
    print(n, " is not a prime number")
    exit() 
if n==2:
    print(n, " is prime number")
    exit()
for i in range(2,n//2+1,1):
    if n%i==0:
        print(n," is not prime number")
        exit() 
print(n,"is a prime number")