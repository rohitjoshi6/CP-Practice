def convert24(str1): 
	if str1[-2:] == "AM" and str1[:2] == "12": 
		return "00" + str1[2:-2] 
        
	elif str1[-2:] == "AM": 
		return str1[:-2] 
	elif str1[-2:] == "PM" and str1[:2] == "12": 
		return str1[:-2] 
	else: 
		return str(int(str1[:2]) + 12) + str1[2:6] 

for i in range(int(input())):
    p=input()
    p=convert24(p)
    #print("p=",p)
    n=int(input())
    ans=""
    for i in range(n):
        string=input()
        a=0
        st1=(convert24(string[:8]))
        #print(st1)
        st2=(convert24(string[9:]))
        #print(st2)
        if p>=st1:
            a+=1
        if p<=st2:
            a+=1
        if a==2:
            ans+="1"
        else:
            ans+="0"                    
    print(ans)
