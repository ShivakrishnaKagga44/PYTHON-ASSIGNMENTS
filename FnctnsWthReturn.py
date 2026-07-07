def process_results(sid,sname,marks,att,assign,extra):
    tot=0
    failsub=[]

    for sub in marks:
        tot=tot+marks[sub]
        if marks[sub]<35:
            failsub+=[sub]

    avg=tot/len(marks)
    avg=avg+(assign*0.10)
    avg=avg+extra

    if att<75:
        avg=avg-5
        attstat="Attendance Below 75%"
    else:
        attstat="Good Attendance"

    if avg>=90:
        grade="A+"
    elif avg>=80:
        grade="A"
    elif avg>=70:
        grade="B"
    elif avg>=60:
        grade="C"
    elif avg>=50:
        grade="D"
    else:
        grade="Fail"

    if len(failsub)==0:
        result="Pass"
    else:
        result="Fail"

    data={
        "Student ID":sid,
        "Student Name":sname,
        "Total Marks":tot,
        "Average":round(avg,1),
        "Grade":grade,
        "Attendance Status":attstat,
        "Failed Subjects":failsub,
        "Result":result
    }

    return data

sid=input("Enter Student ID:")
sname=input("Enter Student Name:")

marks={}
marks["Math"]=int(input("Math:"))
marks["Science"]=int(input("Science:"))
marks["English"]=int(input("English:"))
marks["Computer"]=int(input("Computer:"))
marks["Physics"]=int(input("Physics:"))

att=float(input("Attendance Percentage:"))
assign=float(input("Assignment Score:"))
extra=float(input("Extracurricular Points:"))

data=process_results(sid,sname,marks,att,assign,extra)

print("\nStudent ID:",data["Student ID"])
print("Student Name:",data["Student Name"])
print("Total Marks:",data["Total Marks"])
print("Average:",data["Average"])
print("Grade:",data["Grade"])
print("Attendance Status:",data["Attendance Status"])
print("Failed Subjects:",data["Failed Subjects"])
print("Result:",data["Result"])