n,m,a=map(int,input().split())
 
if n%a==0:
    len=n//a
else:
    len=(n//a)+1
    
if m%a==0:
    wid=m//a
else:
    wid=(m//a)+1
    
print(len*wid)