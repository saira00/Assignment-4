# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

# Department class (aggregation: it uses Employee, but doesn't own it)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: employee passed as reference

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_info()

# Example usage
emp = Employee("Saira", 101)
dept = Department("IT", emp)

dept.show_department_info()
