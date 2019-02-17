#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010
#Notes: Assume the data is input by console.

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

valor=[]
#para cada x em input().split(',')adiciona em itens
itens=[x for x in input().split(',')]
#para cada valor em itens
for p in itens:
    #p é o valor e 2 a base sendo convertidos para int
    intp = int(p, 2)
    #se não é divisivel por 5
    if not intp%5:
        #adiciona na lista
        valor.append(p)

print(','.join(valor))
