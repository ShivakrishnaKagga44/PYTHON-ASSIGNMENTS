i=1
while i<=5:
    j=i
    while j<=5:
        if (i+j)%2==0:
            print(i,j)
        j+=1
    i+=1



i=1
while i<=10:
    j=i
    while j<=10:
        if (i*j)>30:
            print(f"{i} * {j}={i*j}")
        j+=1
    i+=1



while True:
    num=int(input("enter a number : "))
    
    if num==0:
        break
    sum=0
    for i in range(1,num+1):
        
        if num%i==0:
            print(f"The factors are {i}")
            sum+=i
    print(f"Sum={sum}")

n=[12,7,20,9]
for num in n:
    i=1
    count=0 
    while i<=num:
        if i%2==0:
            count+=1
        i+=1
    print(f"{num}->{count}")
     
  
