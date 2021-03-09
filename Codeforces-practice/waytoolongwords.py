n=int(input())
for i in range(n):
    word=input()
    if len(word)>10:
        a=word[0]
        b=word[-1]
        c=len(word[1:-1])
        out=a+str(c)+b
        print(out,end=" ")
    else:
        print(word)