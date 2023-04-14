class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.id} - {self.name} - {self.position} - ${self.salary}"
    


def add_employee(employees, employee):
    employees.append(employee)

def remove_employee(employees, id):
    for index, employee in enumerate(employees):
        if employee.id == id:
            del employees[index]
            break

def search_employee(employees, id):
    for employee in employees:
        if employee.id == id:
            return employee
    return None

def display_employees(employees):
    for employee in employees:
        print(employee)



def main():
    employees = []

    # Add some employees
    add_employee(employees, Employee(1, "John Doe", "Manager", 75000))
    add_employee(employees, Employee(2, "Jane Smith", "Developer", 60000))
    add_employee(employees, Employee(3, "Alice Brown", "Designer", 55000))

    # Display all employees
    print("All employees:")
    display_employees(employees)

    # Search for an employee
    print("\nSearch for employee with ID 2:")
    employee = search_employee(employees, 2)
    print(employee)

    # Remove an employee
    print("\nRemoving employee with ID 1")
    remove_employee(employees, 1)

    # Display all employees again
    print("\nAll employees after removal:")
    display_employees(employees)

if __name__ == "__main__":
    main()
