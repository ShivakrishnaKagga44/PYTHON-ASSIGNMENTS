Student1=list(map(int,input("enter the numbers").split()))
Student2=list(map(int,input("enter the numbers").split()))
total=0
total1=0
for i in Student1:
    total+=i
for j in range(len(Student2)):
    total1+=Student2[j]

print(total)
print(total1)




Sales=list(map(int,input("Enter the sales: ").split()))
total_sales=0
for i in range(len(Sales)):
    for j in range(i+1):
        if Sales[i]==Sales[j]:
            total_sales+=Sales[i]
print(total_sales)


marks=list(map(int,input("Enter the marks: ").split()))
highest=marks[0]
smallest=marks[0]
for i in marks:
    for j in marks:
        if i>highest:
            highest=i
        if i<smallest:
            smallest=j
print(highest)
print(smallest)


Theater=list(map(int,input("Enter the seats booked: ").split()))
booked=0
for i in range(6):
    for j in range(len(Theater)):
        if Theater[j]==1:
            booked+=1
    print(f" Row {i+1} seats booked {booked}")
    break



