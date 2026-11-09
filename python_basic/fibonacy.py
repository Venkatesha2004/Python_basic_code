print("enter the number of terms")
n=int(input())
num1=0
num2=1
if(n<=1):
    print(0)
    exit()
while n!=0:
    print(num1,end=" ")
    temp=num1
    num1=num2
    num2=temp+num2
    n-=1
    
