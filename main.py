class Student:
    def __init__(self):
        print("Enter Student Data\n")

    def set_data(self, name, father_name, student_id, age, mobile_no, father_mobile_no):
        self.name = name
        self.father_name = father_name
        self.student_id = student_id
        self.age = age
        self.mobile_no = mobile_no
        self.father_mobile_no = father_mobile_no

    def display(self):
        print("Name of Student:", self.name)
        print("Name of Student Father:", self.father_name)
        print("Student ID:", self.student_id)
        print("Student Age:", self.age)
        print("Student Mobile No:", self.mobile_no)
        print("Student Father Mobile No:", self.father_mobile_no, "\n")


class Employee(Student):
    def __init__(self):
        super().__init__()
        print("Enter Employee Data\n")

    def set_employee_data(self, employee_name, marital_status, employee_no, employee_age, cnic):
        self.employee_name = employee_name
        self.marital_status = marital_status
        self.employee_no = employee_no
        self.employee_age = employee_age
        self.cnic = cnic

    def display(self):
        print("Name Of Employee:", self.employee_name)
        print("Employee Mobile No:", self.employee_no)
        print("Teacher Father Mobile No:", self.employee_no)
        print("Age of Employee:", self.employee_age)
        print("CNIC of Employee:", self.cnic)
        print("Martial Status of Employee:", self.marital_status, "\n")


class Teacher(Student):
    def __init__(self):
        super().__init__()
        print("Enter Teacher Data\n")

    def set_teacher_data(self, teacher_name, father_name, marital_status, father_mobile_no, mobile_no, age,
                         degree, experience, cnic):
        self.teacher_name = teacher_name
        self.father_name = father_name
        self.marital_status = marital_status
        self.father_mobile_no = father_mobile_no
        self.mobile_no = mobile_no
        self.age = age
        self.degree = degree
        self.experience = experience
        self.cnic = cnic

    def display(self):
        print("Name Of Teacher:", self.teacher_name)
        print("Name of Teacher Father:", self.father_name)
        print("Teacher Mobile No:", self.mobile_no)
        print("Teacher Father Mobile No:", self.father_mobile_no)
        print("Age of Teacher:", self.age)
        print("Degree Of Teacher:", self.degree)
        print("Experience of Teacher:", self.experience)
        print("CNIC of Teacher:", self.cnic)
        print("Martial Status:", self.marital_status, "\n")


def menu():
    welcome_screen()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("||1-Enter New Student Data||")
    print("||2-Enter New Teacher Data||")
    print("||3-Enter New Employee Data||")
    print("||4-See Data From File||")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice()


def choice():
    while True:
        choice = input()
        if choice == '1':
            enter_student_data()
        elif choice == '2':
            enter_teacher_data()
        elif choice == '3':
            enter_employee_data()
        elif choice == '4':
            manager()
        else:
            print("Wrong Input. Try Again.")


def welcome_screen():
    print("\n")
    print("  0     0   000000   0        000000  000000  00   00  000000")
    print("  0     0   0        0        0       0    0  0 0 0 0  0     ")
    print("  0  0  0   000000   0        0       0    0  0  0  0  000000")
    print("  0 0 0 0   0        0        0       0    0  0     0  0     ")
    print("  00   00   000000   000000   000000  000000  0     0  000000")
    print("\n")
    print("--------------------------------------------------------------")
    print("PIR MEHR ALI SHAH ARID AGRICULTURAL UNIVERSITY DATABASE SYSTEM")
    print("--------------------------------------------------------------")
    print("Group Members:\n")
    print("||FAISAL Khan AKA LHF\n\n")


def enter_student_data():
    student_data = Student()
    name = input("Enter Student Name: ")
    father_name = input("Enter Student Father Name: ")
    student_id = input("Enter Student ID: ")
    age = input("Enter Student Age: ")
    mobile_no = input("Enter Student Mobile No: ")
    father_mobile_no = input("Enter Student Father Mobile No: ")

    student_data.set_data(name, father_name, student_id, age, mobile_no, father_mobile_no)

    with open("Student Data.txt", "a") as file:
        file.write(f"Name Of Student: {name}\n")
        file.write(f"Name Of Father: {father_name}\n")
        file.write(f"Name Of Student ID: {student_id}\n")
        file.write(f"Name Of Student Age: {age}\n")
        file.write(f"Name Of Student Mobile No.: {mobile_no}\n")
        file.write(f"Name Of Father Mobile No.: {father_mobile_no}\n\n")

    print("\nThanks For The Data\n")
    student_data.display()


def enter_employee_data():
    employee_data = Employee()
    employee_name = input("Enter Employee Name: ")
    marital_status = input("Enter Employee Martial Status: ")
    employee_no = input("Enter Employee Mobile No: ")
    employee_age = input("Enter Employee Age: ")
    cnic = input("Enter CNIC of Employee: ")

    employee_data.set_employee_data(employee_name, marital_status, employee_no, employee_age, cnic)

    with open("Employee Data.txt", "a") as file:
        file.write(f"Name Of Employee: {employee_name}\n")
        file.write(f"Employee Mobile No.: {employee_no}\n")
        file.write(f"Employee Age: {employee_age}\n")
        file.write(f"Employee Martial Status: {marital_status}\n\n")

    print("\nThanks For The Data\n")
    employee_data.display()


def enter_teacher_data():
    teacher_data = Teacher()
    teacher_name = input("Enter Teacher Name: ")
    father_name = input("Enter Teacher Father Name: ")
    marital_status = input("Enter Teacher Martial Status: ")
    father_mobile_no = input("Enter Teacher Father Mobile No: ")
    mobile_no = input("Enter Teacher Mobile No: ")
    age = input("Enter Age of Teacher: ")
    degree = input("Enter Degree Of Teacher: ")
    experience = input("Enter Experience of Teacher: ")
    cnic = input("Enter CNIC of Teacher: ")

    teacher_data.set_teacher_data(teacher_name, father_name, marital_status, father_mobile_no, mobile_no, age,
                                  degree, experience, cnic)

    with open("Teacher Data.txt", "a") as file:
        file.write(f"Name Of Teacher: {teacher_name}\n")
        file.write(f"Name of Teacher Father: {father_name}\n")
        file.write(f"Teacher Mobile No: {mobile_no}\n")
        file.write(f"Teacher Father Mobile No: {father_mobile_no}\n")
        file.write(f"Age of Teacher: {age}\n")
        file.write(f"Degree Of Teacher: {degree}\n")
        file.write(f"Experience of Teacher: {experience}\n")
        file.write(f"CNIC of Teacher: {cnic}\n")
        file.write(f"Martial Status: {marital_status}\n\n")

    print("\nThanks For The Data\n")
    teacher_data.display()


def manager():
    while True:
        print("1) See Student Data")
        print("2) See Teacher Data")
        print("3) See Employee Data")
        print("4) Go Back To Main Menu")
        option = input()
        if option == '1':
            students()
        elif option == '2':
            teachers()
        elif option == '3':
            employees()
        elif option == '4':
            menu()
        else:
            print("Invalid option. Try again.")


def students():
    while True:
        print("\n1) List of All Students")
        print("2) Go to Menu")
        option = input()
        if option == '1':
            with open("Student Data.txt", "r") as file:
                print(file.read())
            input("\nPress Enter to go to the menu...")
            menu()
        elif option == '2':
            menu()
        else:
            print("Invalid option. Try again.")


def employees():
    while True:
        print("\n1) List of All Employees")
        print("2) Go to Menu")
        option = input()
        if option == '1':
            with open("Employee Data.txt", "r") as file:
                print(file.read())
            input("\nPress Enter to go to the menu...")
            menu()
        elif option == '2':
            menu()
        else:
            print("Invalid option. Try again.")


def teachers():
    while True:
        print("\n1) List of All Teachers")
        print("2) Go to Menu")
        option = input()
        if option == '1':
            with open("Teacher Data.txt", "r") as file:
                print(file.read())
            input("\nPress Enter to go to the menu...")
            menu()
        elif option == '2':
            menu()
        else:
            print("Invalid option. Try again.")


def main():
    menu()


if __name__ == "__main__":
    main()
