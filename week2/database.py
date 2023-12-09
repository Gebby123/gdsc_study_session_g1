students = []

def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    # You can collect any other relevant details here
    
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    students.append(student)
    print("Student added successfully!")

def view_student():
    name = input("Enter student's name: ")
    for student in students:
        if student['name'] == name:
            print("Student Details:")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            return
    print("Student not found!")

def list_all_students():
    print("List of all students:")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
        print("")

def update_student():
    name = input("Enter student's name: ")
    for student in students:
        if student['name'] == name:
            print("Current Details:")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            
            new_age = input("Enter new age (press enter to keep current age): ")
            new_grade = input("Enter new grade (press enter to keep current grade): ")
            
            if new_age:
                student['age'] = new_age
            if new_grade:
                student['grade'] = new_grade
            
            print("Student information updated successfully!")
            return
    print("Student not found!")

def delete_student():
    name = input("Enter student's name: ")
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")

def main():
    while True:
        print("Student Database")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            list_all_students()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()