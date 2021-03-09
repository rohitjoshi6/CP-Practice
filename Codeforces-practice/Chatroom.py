def said_hello(t):
    s="hello"
    i=0
    for char in t:
        if char==s[i]:
            i+=1
        if i==len(s):
            return True
    return False
    
    
t=input().strip()
print("YES" if said_hello(t) else "NO")
    