word=input()
l1=[]
for char in word:
    l1.append(char)
l2=set(l1)
count=len(l2)
if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")