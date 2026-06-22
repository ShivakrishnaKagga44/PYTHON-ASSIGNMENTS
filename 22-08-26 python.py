
n=1
while n<=10:   # it iterates the condition until the condition is false  whenever n value is less than or equal to 10 
    print(n)   # it will print the values after condition checking
    n+=1       # printing the values and increment the value and again the checks the condition



    


#Implement a condition to print only the even numbers within this range using the continue statement.

for i in range(26):         # for loop we used to iterate the set of instructions within the range function
    if i%2==0:               # getting as single value from the range and checks is it divisible by 2 if it is divisible then it will print
                            # otherwise it again goes to loop and access an another valu until end same process 
        print(i)              # used to print the numbers which are divisible by 2






for i in range(26):                # for loop we used to iterate the set of instructions within the range function
    if i%2==0:                     # getting as single value from the range and checks is it divisible by 2 if it is divisible then it will print
                                   # whenever the i value is 8 then the condition checks 8==8 if it is true then the lopp will terminate 
        if i==8:                   # until the condition not met it will  print the numbers 
            break
        print(i)

