T=int(input())            
letters="abcdefghijklmnop"
for i in range(T):
    N=int(input())
    S=input()
    if N>4:
        out=""
        parts = [S[i:i+4] for i in range(0, len(S), 4)]
        for ele in parts:
            ans=int(ele,2)
            out=out+letters[ans]
        print(out)    
    else:
        ans=int(S,2)
        print(letters[ans]) 