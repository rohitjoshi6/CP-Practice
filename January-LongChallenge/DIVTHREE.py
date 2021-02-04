try:
    
    t = int(input())
    for i in range(t):
        N,K,D = [int(i) for i in input().split()]
        A = [int(i) for i in input().split()]
        
        #maximum contest chef can set the problem
        max_contest = sum(A) // K 
        if max_contest > D:
            print(D)
        else:
            print(max_contest)

except EOFError:
    pass