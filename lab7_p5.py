#build a simple Employee Management System using Python. Store the details of employees in a dictionary where the employee ID is the key and the value is another dictionary containing the employee's name, department, and salary.
#Write a Python program that:
#Stores details of at least 3 employees.
#Takes an employee ID as input from the user.
#If the employee ID exists, display the employee's name, department, and salary.
#If the employee ID does not exist, display "Employee not found!".


employees = {
    101: {"name": "Alice Johnson", "department": "HR", "salary": 50000},
    102: {"name": "Bob Smith", "department": "Marketing", "salary": 55000},
    103: {"name": "Charlie Davis", "department": "Engineering", "salary": 70000}
}
emp_id = int(input("Enter employee ID: "))
if emp_id in employees:
    emp = employees[emp_id]
    print("\n--- Employee Details ---")
    print("Name:", emp["name"])
    print("Department:", emp["department"])
    print("Salary: ₹", emp["salary"])
else:
    print("Employee not found!")
