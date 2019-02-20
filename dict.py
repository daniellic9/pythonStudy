d={"letters":0, "digits":0}
str=input()
for x in str:
    if x.isdigit():
        d["digits"]+=1
    elif x.isalpha():
        d["letters"]+=1
    else:
        continue
print("letters",d["letters"])
print("digits",d["digits"])
    
