num=int(input())
ans=[]
for i in range(1,11):
    if num%i==0:
        ans.append(i)
print(max(ans))    

