T=int(input())
for i in range(T):
    n,k=map(int,input().split(" "))
    arr=list(map(int,input().split(" ")))

    if sum(arr)<2*k:
        print(-1)
    else:
        arr.sort(reverse=True)
        if arr[0]>=k and arr[1]>=k:
            print(2)
        else:
            if arr[0]>=k and arr[1]<k:
                sum=0
                for j in range(1,n):
                    sum+=arr[j]
                    if sum>=k:
                        print(j+1)
                        break

            elif arr[0]<k and arr[1]<k:
                l1=[]
                for i in range(n):
                    l1.append(arr[i])
                    if sum(l1)>=k:
                        break
                if len(l1)%2==0:
                    print(len(l1))
                else:
                    l2=[]
                    for ele in l1:
                        l2.append(ele)
                        if sum(l2)>=k:
                            break
                    l3=[i for i in arr + l2 if i not in arr or i not in l2]
                    l4=[]
                    for ele in l3:
                        l4.append(ele)
                        if sum(l4)>=k:
                            print(len(l2)+len(l4))            
                    