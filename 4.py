T=int(input())
ans=[]
for i in range(T):
    N,K,x,y=map(int,input().split(" "))
    A=[(N,N-x+y),(x,N),(0,x-y),(x-y,0)]
    B=[(y,N),(N,N-y+x),(y-x,0),(0,y-x)]
    if x==y:
        print(*(N,N))
    elif x>y:
        for ele in A:
            ans.append(A[K-1])
        print(*ans[0])
    else:
        for ele in B:
            ans.append(B[K-1])
        print(*ans[0])        

