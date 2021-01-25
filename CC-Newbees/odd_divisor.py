T=int(input())
for i in range(T):
    x = int(input())
    for i in range(2, x + 1):
        if x % i == 0:
            if i%2!=0:
                print("YES")
                break
            else:
                print("NO")
                break