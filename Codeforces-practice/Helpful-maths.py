s=input().split("+")
for i in range(len(s)):
    s[i]=int(s[i])

def sort(s):
    for i in range(len(s)):
        for j in range(len(s)-1):
            if s[j]>s[j+1]:
                s[j],s[j+1]=s[j+1],s[j]
                
            else:
                continue
                
   
    
sort(s)

array=[str(x) for x in s]
out="+".join(array)
print(out)
