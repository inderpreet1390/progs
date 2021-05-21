
import time

V='coronavirus'
N='3'
B=['abcde','crnas','onarous']

def func(Bi):
    V='coronavirus'
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
