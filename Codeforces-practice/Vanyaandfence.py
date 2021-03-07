n,h=map(int,input().split(" "))
kids=list(map(int,input().split(" ")))
ct=0
for i in range(n):
    
    if kids[i]<=h:
        ct+=1
    else:
        ct+=2    
print(ct)        