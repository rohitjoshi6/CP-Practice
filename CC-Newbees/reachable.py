T=int(input())
for i in range(T):
    L,R=list(map(int,input().split(" ")))
    if L==R:
        print("1")
    else:    
        num=L*R//2
        print(num)
