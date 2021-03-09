n=int(input())
X=0

for i in range(0,n):
    operation=input()
    
    if "+" in operation:
        X=X+1
        
    if "-" in operation:
        X=X-1
        
print(X)
        