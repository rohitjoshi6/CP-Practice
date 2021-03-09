n=int(input())
l1=list(map(int, input().split(" ")))
length=1
max_length=1

for i in range(1,n):
    if l1[i]>=l1[i-1]:
        length+=1
    else:
        length=1
        
    max_length=max(max_length,length)
    
print(max_length)    