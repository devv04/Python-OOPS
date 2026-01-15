class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        print(f"Employee Created: {self.emp_id}, {self.name}, {self.salary}")

    def display(self):
        print(f"Name is: {self.name}, Employee Id: {self.emp_id}, earns a salary of: {self.salary} per month")

    def annual_salary(self):
        return self.salary*12
    
E1=Employee(1,"dev",82000)
E2=Employee(2,"Kashika",38000)

E1.display()
print(f"Annual Salary of {E1.name}: {E1.annual_salary()}")
E2.display()
print(f"Annual Salary of {E2.name}: {E2.annual_salary()}")