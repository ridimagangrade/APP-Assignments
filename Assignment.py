#function using required argument
def student_required(name, roll_no):
    print("Student Name:", name)
    print("Roll No:", roll_no)

#function using keyword argument 
def student_keyword(name, roll_no): 
    print("Student Name:", name)
    print("Roll No:", roll_no)

#function using default argument 
def student_default(name, roll_no, room="SY4"):
    print("Student Name:", name)
    print("Roll No:", roll_no)
    print("Division:", room)

#function using variable length argument
def student_length(*subject):
    print("Favourite Subject:", subject)


#calling function using required argument 
name=input("Enter Student Name: ")
roll_no=int(input("Enter Roll NO: "))
student_required(name, roll_no)

#calling function using keyword argument
name=input("\nEnter Student Name: ")
roll_no=int(input("Enter Roll No: "))
student_keyword(name=name, roll_no=roll_no)

#calling function using default argument 
name=input("\nEnter Student Name: ")
roll_no=int(input("Enter Roll No: "))
room=input("Enter Student Class: ")
student_default(name, roll_no, room)

#calling function using variable length argument 
sub1=input("\nEnter 1st Favourite Subject: ")
sub2=input("Enter 2nd Favourite Subject: ")
sub3=input("Enter 3rd Favourite Subject: ")
sub4=input("Enter 4th Favourite Subject; ")
student_length(sub1, sub2, sub3, sub4)
