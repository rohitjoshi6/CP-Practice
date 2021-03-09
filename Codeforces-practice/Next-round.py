n,k=map(int,input().split(" "))
nums=list(map(int,input().split(" ")))
temp=nums[k-1]
count=0
for i in range(0,len(nums)):
  if nums[i]>=temp and nums[i]>0:
    count+=1
 
print(count)