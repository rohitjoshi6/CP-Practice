import re

def isAllPresent(str):

	
	regex = ("^(?=.*[a-z])(?=." +
			"*[A-Z])(?=.*\\d)" +
			"(?=.*[-+_!@#$%^&*., ?]).+$")
	
	
	p = re.compile(regex)

	
	'''if (str == ""):
		print("No")
		return'''

	 
	if(re.search(p, str)) and len(str)>=10:
		print("Yes")
	else:
		print("No")

T=int(input())
for i in range(T):
    str=input()
    isAllPresent(str)
    
    
