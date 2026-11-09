text=input("enter the text\n").lower()
reverse_text=""
for ch in text:
    reverse_text=ch+reverse_text
if text==reverse_text:
    print("palindrome")
else:
    print("not palindrome")


#numbers palindrome 
number=int(input("enter a number\n"))
entered_number=number
sum=0
while number!=0:
    rem=number%10
    sum=sum*10+rem
    number=number//10
if(entered_number==sum):
    print("palindrome")
else:
    print("not palindrome")
    


    