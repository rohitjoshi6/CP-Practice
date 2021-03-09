n=int(input())
occ=0
l=[]
for i in range(n):
    num=list(map(int,input().split(" ")))
    l.append(num)
for i in range(n):
    if l[i].count(1)>=2:
        occ+=1
        
print(occ)        