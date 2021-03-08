def ispanagram(str):
    string="abcdefghijklmnopqrstuvwxyz"
    for char in string:
        if char not in str.lower():
            return False
    return True    

n=int(input())
str=input()
if (ispanagram(str)==True):
    print("YES")
else:
    print("NO")    
