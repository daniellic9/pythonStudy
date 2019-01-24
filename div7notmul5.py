#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
l=[]

def div7(n):
    if n%7==0:
        return n
    else:
        return -1

def notDiv5(n):
    if n%5==0:
        return -1
    else:
        return n

def div7notmul5(n):
    if (div7(n)&notDiv5(n))>0:
        return n

for i in range(2000, 3201):
    if(div7(i) and notDiv5(i))>0:
        l.append(str(i))
        
print (', '.join(l)  )
