a,b,c=0,0,1
n=int(input())
print("Fibonacci Series is: ")
for i in range(n):
    a=b
    b=c
    c=a+b
    print(a,end=" ")