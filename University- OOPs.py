class Person:
    university_name = "Andhra University" 

    def __init__(self, name, age, Edu_BG, Gender, Department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.Gender = Gender
        self.Department = Department

    def display_info(self):
        """Method to be overridden"""
        pass


# ---------------- Student ---------------- #

class Student(Person):
    student_count = 0

    def __init__(self, name, age, student_id, course, Year_, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__student_id = student_id
        self.course = course
        self.Year_ = Year_

        Student.student_count += 1

    def display_info(self):
        print("\n------ Student Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Student ID :", self.__student_id)
        print("Course     :", self.course)
        print("Year       :", self.Year_)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    def get_student_id(self):
        return self.__student_id

    @classmethod
    def total_students(cls):
        print("Total Students :", cls.student_count)


# ---------------- Faculty ---------------- #

class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, faculty_id, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__faculty_id = faculty_id

        Faculty.faculty_count += 1

    def display_info(self):
        print("\n------ Faculty Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Faculty ID :", self.__faculty_id)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @staticmethod
    def university_policy():
        print("\nUniversity Policy:")
        print("Codegnan University follows strict academic policies.")

    @classmethod
    def total_faculty(cls):
        print("Total Faculty Members :", cls.faculty_count)

# ---------------- Library ---------------- #

class Library:
    total_books = 100

    def __init__(self, student_name, book_name):
        self.student_name = student_name
        self.book_name = book_name

    def issue_book(self):
        print(f"\n{self.book_name} has been issued to {self.student_name}")

    def return_book(self):
        print(f"{self.student_name} has returned {self.book_name}")


# ---------------- Attendance ---------------- #

class Attendance:
    def __init__(self, student_name, total_classes, present):
        self.student_name = student_name
        self.total_classes = total_classes
        self.present = present

    def attendance_percentage(self):
        percentage = (self.present / self.total_classes) * 100
        print(f"\nAttendance of {self.student_name} : {percentage:.2f}%")

    def display_attendance(self):
        print("\n------ Attendance Details ------")
        print("Student Name :", self.student_name)
        print("Total Classes:", self.total_classes)
        print("Present      :", self.present)
        print("Absent       :", self.total_classes - self.present)


# ---------------- Fee ---------------- #

class Fee:
    def __init__(self, student_name, tuition_fee, hostel_fee):
        self.student_name = student_name
        self.tuition_fee = tuition_fee
        self.hostel_fee = hostel_fee

    def total_fee(self):
        total = self.tuition_fee + self.hostel_fee
        print(f"\nTotal Fee of {self.student_name} : ₹{total}")

    def fee_status(self):
        print(f"{self.student_name}'s Fee Status : Paid")


# ---------------- Examination ---------------- #

class Examination:
    def __init__(self, exam_name, subject, exam_date):
        self.exam_name = exam_name
        self.subject = subject
        self.exam_date = exam_date

    def display_exam(self):
        print("\n------ Examination Details ------")
        print("Exam Name :", self.exam_name)
        print("Subject   :", self.subject)
        print("Date      :", self.exam_date)

    @staticmethod
    def exam_rules():
        print("\nExam Rules")
        print("1. Carry Hall Ticket")
        print("2. No Mobile Phones")
        print("3. Report 30 Minutes Early")


# ---------------- Result ---------------- #

class Result:
    def __init__(self, student_name, subject, marks):
        self.student_name = student_name
        self.subject = subject
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            grade = "A+"
        elif self.marks >= 80:
            grade = "A"
        elif self.marks >= 70:
            grade = "B"
        elif self.marks >= 60:
            grade = "C"
        elif self.marks >= 35:
            grade = "Pass"
        else:
            grade = "Fail"

        print("\n------ Result ------")
        print("Student :", self.student_name)
        print("Subject :", self.subject)
        print("Marks   :", self.marks)
        print("Grade   :", grade)

# ---------------- Objects ---------------- #

student1 = Student("Rahul Sharma",21,"CNU12345","Computer Science",2026,"Intermediate","Male","IT")
student2 = Student("Ananya Reddy",22,"CNU67890","Data Science",2026,"Intermediate","Female","IT")

faculty1 = Faculty("Dr. Ravi Kumar",45,"F001","AI & ML","PhD","Male")
faculty2 = Faculty("Dr. Meera Srinivas",50,"F002","Cybersecurity","PhD","Female")

library = Library("Rahul Sharma", "Python Programming")

attendance = Attendance("Rahul Sharma", 100, 92)

fee = Fee("Rahul Sharma", 50000, 20000)

exam = Examination("Semester End", "Python", "20-Dec-2026")

result = Result("Rahul Sharma", "Python", 91)

# ---------------- Output ---------------- #

student1.display_info()
student2.display_info()

print("\nStudent ID:", student1.get_student_id())

faculty1.display_info()
faculty2.display_info()

Faculty.university_policy()

Student.total_students()
Faculty.total_faculty()

library.issue_book()
library.return_book()

attendance.display_attendance()
attendance.attendance_percentage()

fee.total_fee()
fee.fee_status()

exam.display_exam()
Examination.exam_rules()

result.grade()
