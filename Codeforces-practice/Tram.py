def tramCapacity():
    n = int(input().strip())
    pout, pin = map(int,input().strip().split())
    sm = pin
    mx = pin
    for i in range(n-1):
        pout, pin = map(int,input().strip().split())
        sm = sm - pout + pin
        if sm > mx:
            mx = sm
    return mx


if __name__ == "__main__":
    print(tramCapacity())