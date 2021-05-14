n=int(input("Enter the number: "))
i=2
while(i<n):
    if(n%i==0):
        print(n," is not prime number")
        break
    else:
        i+=1
if(i==n):
    print(n," is prime number")