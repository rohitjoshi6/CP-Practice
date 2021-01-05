T=int(input())
ans=[]
for i in range(T):
    N,K,x,y=map(int,input().split(" "))
    A=[(N,N-x+y),(x,N),(0,x-y),(x-y,0)]
    B=[(y,N),(N,N-y+x),(y-x,0),(0,y-x)]
    if x==y:
        ans.append((N,N))
    elif x>y:
        for j in range(K):
            if j==K:
                ans.append(A[K-1])
        
    else:
        for j in range(K):
            if j==K:
                ans.append(B[K-1])

for i in range(T):
    print(*ans[i])                

