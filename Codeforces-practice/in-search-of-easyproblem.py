n=int(input())
res=list(map(int,input().split(" ")))
cnt=0
for i in range(len(res)):
    if res[i]==1:
        cnt+=1
if cnt!=0:
    print('Hard')
else:
    print("Easy")
        