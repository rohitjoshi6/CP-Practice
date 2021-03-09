class Football:
    def solve(self,footballers):
        if(len(footballers)<7):
            return "NO"
        
        import re
        match_ones = re.search(r'\d*1111111\d*',footballers)
        match_zeroes = re.search(r'\d*0000000\d*',footballers)
        
        if(match_ones or match_zeroes):
            return "YES"
        else:
            return "NO"
       
        
        
if __name__ == "__main__":
    footballers = input()
    f = Football()
    print (f.solve(footballers))