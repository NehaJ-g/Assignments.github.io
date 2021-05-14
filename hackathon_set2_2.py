T=int(input())

for i in range(T):
    N=int(input())
    lst=list(map(int,input().split()))
    lst.reverse()
    for num in lst:
        print(num,end=" ")