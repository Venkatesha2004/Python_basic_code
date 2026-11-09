num=int(input("enter a number"))
power=len(str(num))
temp=num
res=0
while num!=0:
    print(num, power,res)
    res=res+(num%10)**power
    num //=10
if res==temp:
    print(temp," is an amstrongnumber")
else:
    print(temp," is not an amstrongnumber")