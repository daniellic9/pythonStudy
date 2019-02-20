#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

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
    
