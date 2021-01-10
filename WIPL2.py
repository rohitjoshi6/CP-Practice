T=int(input())
ans=[]
for i in range(T):
    list1=[]
    list2=[]
    N,K=map(int,input().split(" "))
    nums=list(map(int,input().split(" ")))
    nums.sort(reverse=True)

    if sum(nums)>=2*K:
        arr=[]
        for i in range(len(nums)):
            arr.append(nums[i])
            if sum(arr)>=2*K:
                break
            else:
                continue
        
        list1.append(arr[0])
        arr.pop(0)
        for ele in arr[::-1]:
            list1.append(ele)
            if sum(list1)>=K:
                break
             

        list2=[i for i in arr + list1 if i not in arr or i not in list1]
        if sum(list2)>=K:
            out=len(list1)+len(list2)
            ans.append(out)
        else:
            final=(list(list(set(nums)-set(arr)) + list(set(arr)-set(nums))))
            for i in range(len(final)):
                list2.append(final[i])
                if sum(list2)>=K:
                    out=len(list1)+len(list2)
                    ans.append(out)
                else:
                    continue

    else:
        print(-1)
for ele in ans:
    print(ele)        