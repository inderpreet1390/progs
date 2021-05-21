
import time

V=input() #take input from user for the main string
N=int(input()) #input for number of strings
B=list(map(str,input())) #strings which we need to check if they are substring for V

#V='coronavirus'
#N=3
#B=['abcde','crnas','onarous']

def func(Bi):
    
    c=0
    pos=0
    l=len(Bi)
    for i in range(l):
        for j in range(pos,len(V)):
            if(Bi[i]==V[j]):
                c=c+1
                pos=j
                break
            elif(j==len(V)-1):
                c=0
                pos=0
                break
    if(c==l):
        return "POSITIVE"
    else:
        return "NEGATIVE"

start_time = time.time()
for _ in range(100):
    xyz=list(map(func,B))
    for i in range(len(xyz)):
        print(xyz[i])

print("--- %s seconds ---" % (time.time() - start_time))
