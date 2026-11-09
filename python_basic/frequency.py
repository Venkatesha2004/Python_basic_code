text=input("enter a text")
dict={}
for ch in text:
    dict[ch]=dict.get(ch,0)+1
for k,v in dict.items():
    print(k,"=",v,end="")
    
