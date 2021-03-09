m,n=map(int,input().split(" "))
num=m*n
if num%2==0:
    print(num//2)
else:
    out=(num-1)//2
    print(out)