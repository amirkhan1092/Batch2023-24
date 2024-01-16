class Employee: 
    def __init__(self, name, emp_id, salary=0, dept='CSE'):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.dept = dept 
    def getDetails(self):
        return f'''
        Name: {self.name}
        Id:{self.emp_id}
        Salary: {self.salary}
        Department: {self.dept}
            '''
    def update_salary(self, newsalary):
        self.salary = newsalary

# main code or driver code 
emp1 = Employee('ravi', 'gla1223', 12000, 'ece')
emp2 = Employee('saket', 'gla1133', 14100, 'cse')

print(emp1.getDetails())





