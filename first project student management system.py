
# Online IDE - Code Editor, Compiler, Interpreter

students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    
    student = {"name" : name, "roll": roll, "course": course}
    students.append(student)
    print("Student added successfully!")
    
def view_students():
    if not students:
        print("No students found")
    else:
        for s in students:
            print(s)

def delete_students():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Studennt deleted")
            retyrn 
    print("Student not found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
    
