try :
    
    t = int(input())
    for i in range(t):
        N, M = [int(i) for i in input().split()]
        A = [int(i) for i in input().split()]
        B = [int(i) for i in input().split()]
        A.sort()
        B.sort()
        if sum(A) > sum(B):  #if John has already greater vote then no need to swap.
            print(0)
            continue
        low = 0
        high = M - 1
        swap = 0
        while low < N and high >= 0:
            A[low],B[high] = B[high],A[low]  #swap only the minimum vote of John with maximum vote of Jack which makes the higher probability of John to win and require less swapping
            swap = swap + 1
            if sum(A) > sum(B):  #if the total vote of John is greater than total vote of Jack then break the loop, we got the required answer
                print(swap)
                break
            low = low + 1
            high = high - 1
        if sum(A) <= sum(B):  #after swapping also if the total vote of John is less than total vote of Jack then there is no chance that John will win
            print(-1)
except EOFError:
    pass