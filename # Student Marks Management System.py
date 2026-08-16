

students = []

while True:
    print("\n===== STUDENT MARKS MANAGEMENT SYSTEM =====")
    print("1. Insert Student")
    print("2. Delete Student")
    print("3. Display Students")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))

        student = [name, marks]
        students.append(student)

        print("Student inserted successfully!")

    
    elif choice == 2:
        name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student[0].lower() == name.lower():
                students.remove(student)
                found = True
                print("Student deleted successfully!")
                break

        if not found:
            print("Student not found!")

    
    elif choice == 3:
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\n----- Student Records -----")

            for i, student in enumerate(students, start=1):
                print("Student", i)
                print("Name  :", student[0])
                print("Marks :", student[1])
                print("---------------------------")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")