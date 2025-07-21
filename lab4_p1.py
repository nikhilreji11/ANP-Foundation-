#Add and remove student names from a list

students = []
def add_student(name):
    students.append(name)
    print(f"{name} added successfully!")
def remove_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} removed successfully!")
    else:
        print(f"{name} not found in the list.")
add_student("Alice")
add_student("Bob")
add_student("Charlie")
print("Student list:", students)
remove_student("Bob")
print("Updated student list:", students)
