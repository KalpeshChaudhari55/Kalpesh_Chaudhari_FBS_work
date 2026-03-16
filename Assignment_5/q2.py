#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.
n=int(input("enter the number of student: "))
total_percentage = 0
for i in range(n):
    print("enter the marks of student",i+1)

    m1 = int(input("enter the subject 1: "))
    m2 = int(input("enter the subject 2: "))
    m3 = int(input("enter the subject 3: "))
    m4 = int(input("enter the subject 4: "))
    m5 = int(input("enter the subject 5: "))
    total = m1+m2+m3+m4+m5
    percentage  = total/5
    print("percentage",percentage)
    total_percentage = total_percentage + percentage
avg = total_percentage/n
print("average percentage of student: ",avg)