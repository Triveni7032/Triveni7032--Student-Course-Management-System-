import json


FILE_NAME = "students.json"


# Read students from JSON file
def load_students():

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)

        return students

    except FileNotFoundError:
        print("JSON file not found.")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return []


# Save students to JSON file
def save_students(students):

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Display all students
def view_students():

    students = load_students()

    print("\n===== STUDENT DETAILS =====")

    for student in students:

        print(
            "ID:", student["student_id"],
            "| Name:", student["name"],
            "| Course:", student["course"],
            "| Marks:", student["marks"]
        )


# Search student
def search_student():

    students = load_students()

    student_id = int(input("\nEnter student ID: "))

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Found")

            print("ID:", student["student_id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

            return

    print("Student not found.")


# Add new student
def add_student():

    students = load_students()

    student_id = int(input("\nEnter student ID: "))
    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    new_student = {
        "student_id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(new_student)

    save_students(students)

    print("Student added successfully.")


# Update student marks
def update_marks():

    students = load_students()

    student_id = int(input("\nEnter student ID: "))

    for student in students:

        if student["student_id"] == student_id:

            new_marks = int(input("Enter new marks: "))

            student["marks"] = new_marks

            save_students(students)

            print("Marks updated successfully.")

            return

    print("Student not found.")


# Find students with marks above 80
def high_scorers():

    students = load_students()

    print("\n===== STUDENTS ABOVE 80 MARKS =====")

    found = False

    for student in students:

        if student["marks"] > 80:

            print(
                student["name"],
                "-",
                student["marks"]
            )

            found = True

    if not found:
        print("No students found.")


# Main menu
def main():

    while True:

        print("\n==============================")
        print(" STUDENT COURSE MANAGEMENT")
        print("==============================")

        print("1. View Students")
        print("2. Search Student")
        print("3. Add Student")
        print("4. Update Marks")
        print("5. View High Scorers")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_students()

        elif choice == "2":
            search_student()

        elif choice == "3":
            add_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            high_scorers()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()