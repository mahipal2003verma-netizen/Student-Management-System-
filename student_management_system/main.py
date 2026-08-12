print("=================================")
print("     STUDENT MANAGEMENT SYSTEM")
print("=================================")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n----- ADD STUDENT -----")

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        roll_no = input("Enter roll number: ")
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        student = {
            "name": name,
            "age": age,
            "roll_no": roll_no,
            "course": course,
            "marks": marks,
            "grade": grade
        }

        students.append(student)

        print("\nStudent added successfully! ✅")
        print("Grade:", grade)

    elif choice == "2":
        print("\n----- ALL STUDENTS -----")

        if len(students) == 0:
            print("No students found.")

        else:
            for student in students:
                print("\nName:", student["name"])
                print("Age:", student["age"])
                print("Roll No:", student["roll_no"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                print("Grade:", student["grade"])

    elif choice == "3":
        print("\n----- SEARCH STUDENT -----")

        roll_no = input("Enter roll number: ")

        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                print("\nStudent Found! ✅")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Roll No:", student["roll_no"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                print("Grade:", student["grade"])

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":
        print("\n----- DELETE STUDENT -----")

        roll_no = input("Enter roll number: ")

        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                students.remove(student)

                print("Student deleted successfully! ✅")

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "5":
        print("\nThank you for using Student Management System! 👋")
        break

    else:
        print("\nInvalid choice! Please try again.")