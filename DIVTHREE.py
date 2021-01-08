T=int(input())
ans=[]
for i in range(T):
    N,K,D=map(int,input().split(" "))
    num=list(map(int,input().split(" ")))
    num1=sum(num)
    out=num1//K
    if out>D:
        ans.append(D)
    else:
        ans.append(out)
for ele in ans:
    print(ele)            
    