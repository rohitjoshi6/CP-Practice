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

##########################################

T=int(input())
for x in range(T):
    n,k,x,y=map(int,input().split(" "))
    
    if (x==y):
        print(n,n)
    else:
        if (x>y):
            col1=[n,y+(n-x)]
            col2=[col1[1],n]
            col3=[0,n-col2[0]]
            col4=[col3[1],0]
        else:
            col1=[x+(n-y),n]
            col2=[n,col1[0]]
            col3=[n-col2[1],0]
            col4=[0,col3[0]]
        ans=[col4,col1,col2,col3]
        res=ans[k%4]
        print(res[0],res[1])

