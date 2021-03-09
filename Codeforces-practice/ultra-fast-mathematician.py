n=input()
m=input()
ans=[]
for i in range(len(n)):
  if n[i]==m[i]:
    ans.append(str(0))
  else:
    ans.append(str(1))
print("".join(ans))  