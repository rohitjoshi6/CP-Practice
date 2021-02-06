T=int(input())
for i in range(T):
    n=int(input())
    nums=list(map(int,input().split(" ")))
    c=max(nums)
    a=min(nums)
    print(2*(c-a))