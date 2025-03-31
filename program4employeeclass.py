class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_info(self):
        return f"Name: {self.name}, ID: {self.id_number}, Department: {self.department}, Title: {self.job_title}"


# Main program
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Display employee details
print(employee1.display_info())
print(employee2.display_info())
print(employee3.display_info())
