print("enter the number of elements")
n=int(input())
if(n<2):
    print("please enter more than 1 number")
    exit()
list=list()
for i in range(n):
    list.append(int(input()))
largest=float("-inf")
second_largest=float('-inf')
for num in list:
    if num>largest:
        second_largest=largest
        largest=num
        
    elif second_largest<num and largest!=num:
        second_largest=num
print(second_largest)