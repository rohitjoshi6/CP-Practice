def solve(year):
    while(True):
        year = str(int(year)+1)
        if(len(set(year))==4):
            return year

print (solve(input()))
