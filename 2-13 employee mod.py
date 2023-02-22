'''
Emily Eckstein
2/13/23
M05

Write a program that allows you to manage information about employees of a company.
Get employee data from the user, calculate the average salary of all employees, determine the highest paid employee,
and find all employees in a specific department.
'''

def get_employee_data():
    employee_data = []
    while True:
        name = input("Enter employee name (or press enter to finish): ")
        if name == "":
            break
        salary = float(input("Enter employee salary: "))
        department = input("Enter employee department: ")
        employee_data.append({"name": name, "salary": salary, "department": department})
    return employee_data

def calculate_average_salary(employee_data):
    total_salary = 0
    for employee in employee_data:
        total_salary += employee["salary"]
    return round(total_salary / len(employee_data), 2)

def find_highest_paid_employee(employee_data):
    highest_paid_employee = None
    highest_salary = 0
    for employee in employee_data:
        if employee["salary"] > highest_salary:
            highest_paid_employee = employee["name"]
            highest_salary = employee["salary"]
    return highest_paid_employee

def find_employees_by_department(employee_data, department):
    employees_in_department = []
    for employee in employee_data:
        if employee["department"] == department:
            employees_in_department.append(employee["name"])
    return employees_in_department

def main():
    employee_data = get_employee_data()
    avg_salary = calculate_average_salary(employee_data)
    highest_paid = find_highest_paid_employee(employee_data)
    print("Average Salary:", avg_salary)
    print("Highest Paid Employee:", highest_paid)
    department = input("Enter department to find employees in: ")
    employees_in_department = find_employees_by_department(employee_data, department)
    print("Employees in", department, ":", employees_in_department)

if __name__ == '__main__':
    main()