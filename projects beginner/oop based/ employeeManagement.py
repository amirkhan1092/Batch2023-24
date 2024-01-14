class Employee:
    def __init__(self, name, employee_id, position, salary):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def display_details(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nPosition: {self.position}\nSalary: {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary
        return f"Salary updated for {self.name}. New salary: {self.salary}"


# Example usage:
employee1 = Employee("Ravi", 101, "Software Engineer", 80000)
employee2 = Employee("Saket", 102, "Data Scientist", 90000)

# Display employee details
print("Employee 1 Details:")
print(employee1.display_details())
print("\nEmployee 2 Details:")
print(employee2.display_details())

# Update salary
new_salary = 85000
update_message = employee1.update_salary(new_salary)
print("\n", update_message)

# Display updated details
print("\nEmployee 1 Updated Details:")
print(employee1.display_details())
