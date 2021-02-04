try:
    
    t = int(input())
    for i in range(t):
        n,k,x,y = [int(i) for i in input().split()]
        if x == y:      #sample case 1
            print(n,n)
        else:
            if x > y:
                quad = [(n,y+n-x),(y+n-x,n),(0,x-y),(x-y,0)]  #coordinates of 1st, 2nd, 3rd and 4th Quadrant respectively
            else:
                quad = [(x+n-y,n),(n,n-y+x),(y-x,0),(0,y-x)]  
            
            #when the ball hits the sides for the Kth time, the ball will stop in one of the Quadrant and coordinates is obtained as
            cord = quad[(k-1) % 4]
            print(cord[0],cord[1])
except EOFError:
    pass