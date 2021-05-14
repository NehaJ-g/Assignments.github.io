n=int(input())
socks_list=list(map(int,input().split()))
socks_set=set(socks_list)
pair=0
for num in socks_set:
    pair+=(socks_list.count(num))//2
print(pair)
    