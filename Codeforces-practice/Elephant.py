steps=(5,4,3,2,1)

def solve(n):

    stepsCount = 0
    while n > 0:

        for step in steps:

            if n >= step:
                stepsCount += 1
                n -= step
                break

    return stepsCount
    
n=int(input())
print(solve(n))
    