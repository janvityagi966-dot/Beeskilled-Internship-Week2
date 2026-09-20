students = {}


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    students[student_id] = {
        "name": name,
        "course": course,
        "marks": marks,
    }
    print("Student added successfully.")


def display_students():
    if not students:
        print("No students available.")
        return

    print("\nStudent List:")
    for student_id, info in students.items():
        print(f"ID: {student_id}, Name: {info['name']}, Course: {info['course']}, Marks: {info['marks']}")


def search_student():
    student_id = input("Enter Student ID to search: ")

    if student_id in students:
        info = students[student_id]
        print(f"\nStudent Found:")
        print(f"ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Course: {info['course']}")
        print(f"Marks: {info['marks']}")
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    if student_id in students:
        students[student_id]["name"] = input("Enter New Name: ")
        students[student_id]["course"] = input("Enter New Course: ")
        students[student_id]["marks"] = input("Enter New Marks: ")
        print("Student record updated.")
    else:
        print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted.")
    else:
        print("Student not found.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
