class stringtask:
    def solve(self,str):
        return "".join("."+char.lower() for char in str if char.lower() not in 'aeiouy')
str=input()
st=stringtask()
print(st.solve(str))
