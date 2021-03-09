n=int(input())
game=input()
l1=0
l2=0
for i in range(n):
    if game[i]=="A":
        l1+=1
    else:
        l2+=1
        
if l1>l2:
    print("Anton")
elif l1==l2:
    print("Friendship")
else:
    print("Danik")