#4.Write a python program and iterate the given tuples
#Input:
#employee1= ("John Doe", 101, "Human Resources", 60000)
#employee2 = ("Alice Smith", 102, "Marketing", 55000)
#employee3 = ("Bob Johnson", 103, "Engineering", 75000)
#Output:
#Employee Records:
#Name: John Doe
#Employee ID: 101
#Department: Human Resources
#Salary: $60000

#Name: Alice Smith
#Employee ID: 102
#Department: Marketing
#Salary: $55000

#Name: Bob Johnson
#Employee ID: 103
#Department: Engineering
#Salary: $75000


employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employees = [employee1, employee2, employee3]
print("Employee Records:")
for emp in employees:
    name, emp_id, department, salary = emp
    print(f"\nName: {name}")
    print(f"Employee ID: {emp_id}")
    print(f"Department: {department}")
    print(f"Salary: ${salary}")
    
