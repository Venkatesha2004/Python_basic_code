text=input("Enter a string")
reverse_string=""
for ch in text:
    reverse_string=ch+reverse_string
print(reverse_string)

#second logic 
reverse_text2=text[::-1]
print(reverse_text2)

#third logic 
print(reversed(text))
reverse_text3="".join(reversed(text))
print(reverse_text3)