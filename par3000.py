array=[]
for num in range(1000, 3001):
    if num%2:
        numS=str(num)
        if(int(numS[0])%2==0) and (int(numS[1])%2==0) and (int(numS[2])%2==0) and (int(numS[3])%2==0):
            array.append(numS)
    num+1
print(",".join(array))

