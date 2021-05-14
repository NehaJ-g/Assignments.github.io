def check(arr,K,N):
    flag=0
    for i in range(N-K):

        if flag==0:
            if arr[i]%2!=0:
                for j in range(i+1,i+K):
                    if arr[j]%2!=0:
                        flag=1
                    else:
                        flag=0
                        break
        else:
            return 'yes'
    return 'no'
    


T=int(input())
result=[]
for i in range(T):
    N,K=map(int,input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    result.append(check(lst,K,N))
for char in result:
    print(char)