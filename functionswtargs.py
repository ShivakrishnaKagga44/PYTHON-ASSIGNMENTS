def sdata(s_id,name):
    print("Student Details")
    print("Student ID:",s_id)
    print("Student Name:",name)

def totmarks(m1,m2,m3,m4,m5):
    total=m1+m2+m3+m3+m5
    print("Total Marks:",total)

def percencalci(m1,m2,m3,m4,m5):
    total=m1+m2+m3+m4+m5
    percentage=total/5
    print("Percentage:",percentage,"%")

def grdchck(m1,m2,m3,m4,m5):
    total=m1+m2+m3+m4+m5
    percentage=total/5
    if percentage>=90 and percentage<=100:
        print("Grade:A")
    elif percentage>=75 and percentage<90:
        print("Grade:B")
    elif percentage>=60 and percentage<75:
        print("Grade:C")
    elif percentage>=40 and percentage<60:
        print("Grade:D")
    else:
        print("Grade:Fail")

def Topmark(m1,m2,m3,m4,m5):
    high=m1
    if m2>high:
        high=m2
    if m3>high:
        high=m3
    if m4>high:
        high=m4
    if m5>high:
        high=m5
    print("Highest Mark:",high)

def lowmark(m1,m2,m3,m4,m5):
    low=m1
    if m2<low:
        low=m2
    if m3<low:
        low=m3
    if m4<low:
        low=m4
    if m5<low:
        low=m5
    print("Lowest Mark:",low)

def porf(m1,m2,m3,m4,m5):
    if m1<35 or m2<35 or m3<35 or m4<35 or m5<35:
        print("Result:Fail")
    else:
        print("Result:Pass")

student_id=input("Enter Student ID:")
name=input("Enter Student Name:")
m1=int(input("Enter Subject 1 Marks:"))
m2=int(input("Enter Subject 2 Marks:"))
m3=int(input("Enter Subject 3 Marks:"))
m4=int(input("Enter Subject 4 Marks:"))
m5=int(input("Enter Subject 5 Marks:"))

sdata(student_id,name)
totmarks(m1,m2,m3,m4,m5)
percencalci(m1,m2,m3,m4,m5)
grdchck(m1,m2,m3,m4,m5)
Topmark(m1,m2,m3,m4,m5)
lowmark(m1,m2,m3,m4,m5)
porf(m1,m2,m3,m4,m5)