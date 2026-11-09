print("Enter a number of elements in the array")
n=int(input())
list=list()
for i in range(n):
    print("enter a element",i)
    list.append(int(input()))

if len(list)!=0:
    min=list[0]
    max=list[0]
    for i in list:
        if max<i:
            max=i
        if min>i:
            min=i
print(min,max)

    