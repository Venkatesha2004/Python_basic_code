print("enter a number of elements")
n=int(input())
list=list()
for i in range(n):
    list.append(int(input()))
print(list)
odd=[num for num in list if num%2!=0 ]
even=[num for num in list if num%2==0 ]
print(odd,even)