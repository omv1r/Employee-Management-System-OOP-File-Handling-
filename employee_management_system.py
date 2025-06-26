
import os
import pickle

class Employee:
    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Role: {self.role}, Salary: {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.pkl"):
        self.filename = filename
        self.employees = self.load_employees()

    def load_employees(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        return {}

    def save_employees(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.employees, file)

    def add_employee(self, emp):
        if emp.emp_id in self.employees:
            print("Employee ID already exists.")
        else:
            self.employees[emp.emp_id] = emp
            self.save_employees()
            print("Employee added.")

    def update_employee(self, emp_id, name=None, role=None, salary=None):
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            if name: emp.name = name
            if role: emp.role = role
            if salary: emp.salary = salary
            self.save_employees()
            print("Employee updated.")
        else:
            print("Employee not found.")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_employees()
            print("Employee deleted.")
        else:
            print("Employee not found.")

    def search_employee(self, emp_id):
        return self.employees.get(emp_id, "Employee not found.")

    def list_employees(self):
        for emp in self.employees.values():
            print(emp)

def main():
    manager = EmployeeManager()
    while True:
        print("\n1. Add\n2. Update\n3. Delete\n4. Search\n5. List\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            emp_id = input("ID: ")
            name = input("Name: ")
            role = input("Role: ")
            salary = input("Salary: ")
            emp = Employee(emp_id, name, role, salary)
            manager.add_employee(emp)
        elif choice == "2":
            emp_id = input("ID to update: ")
            name = input("New name (or press enter to skip): ")
            role = input("New role (or press enter to skip): ")
            salary = input("New salary (or press enter to skip): ")
            manager.update_employee(emp_id, name or None, role or None, salary or None)
        elif choice == "3":
            emp_id = input("ID to delete: ")
            manager.delete_employee(emp_id)
        elif choice == "4":
            emp_id = input("ID to search: ")
            print(manager.search_employee(emp_id))
        elif choice == "5":
            manager.list_employees()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
