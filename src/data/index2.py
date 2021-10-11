import liba
import decimal
from math import *
numbers = []
f = open("data1","r")
for line in f:
    numbers.append(long(line))
f.close()
divisers = [None] * len(numbers)
for i in range(0,len(numbers)-1):
    for j in range(i+1,len(numbers)):
        res = liba.GCD(numbers[i],numbers[j])
        if res > 1 and res != numbers[i] and res != numbers[j]:
            print i,j,res
            divisers[i] = [res,numbers[i] / res]
            divisers[j] = [res,numbers[j] / res]
f = open('done1.res', "w")
for i in range(len(divisers)):
    if divisers[i] != None:
        f.write(str(i) + '\n')
        f.write(str(divisers[i][0]) + '\n')
        f.write(str(divisers[i][1]) + "\n\n")
f.close()
