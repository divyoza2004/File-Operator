class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    def display(self):
        print("\n----- Person Details -----")
        print("Name :", self.name)
        print("Age  :", self.age)

class Employee(Person):
    def __init__(self, emp_id="", name="", age=0, salary=0):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary
    def __del__(self):
        print("Employee object deleted.")
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id
    def set_salary(self, salary):
        self.__salary = salary
    def get_emp_id(self):
        return self.__emp_id
    def get_salary(self):
        return self.__salary
    def display(self):
        print("\n----- Employee Details -----")
        print("Employee ID :", self.__emp_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Salary      :", self.__salary)

class Manager(Employee):
    def __init__(self, emp_id="", name="", age=0, salary=0, department=""):
        super().__init__(emp_id, name, age, salary)
        self.department = department
    def display(self):
        print("\n----- Manager Details -----")
        print("Employee ID :", self.get_emp_id())
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Salary      :", self.get_salary())
        print("Department  :", self.department)

class Developer(Employee):
    def __init__(self, emp_id="", name="", age=0, salary=0, language=""):
        super().__init__(emp_id, name, age, salary)
        self.language = language
    def display(self):
        print("\n----- Developer Details -----")
        print("Employee ID           :", self.get_emp_id())
        print("Name                  :", self.name)
        print("Age                   :", self.age)
        print("Salary                :", self.get_salary())
        print("Programming Language  :", self.language)

person_obj = None
employee_obj = None
manager_obj = None
developer_obj = None
print("========== Employee Management System ==========")
while True:
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Check issubclass()")
    print("7. Exit")
    choice = int(input("\nEnter your choice: "))
    match choice:
        case 1:
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            person_obj = Person(name, age)
            print("\nPerson created successfully!")
        case 2:
            emp_id = input("Enter Employee ID : ")
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            salary = float(input("Enter Salary : "))
            employee_obj = Employee(emp_id, name, age, salary)
            print("\nEmployee created successfully!")
        case 3:
            emp_id = input("Enter Employee ID : ")
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            salary = float(input("Enter Salary : "))
            department = input("Enter Department : ")
            manager_obj = Manager(emp_id, name, age, salary, department)
            print("\nManager created successfully!")

        case 4:
            emp_id = input("Enter Employee ID : ")
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            salary = float(input("Enter Salary : "))
            language = input("Enter Programming Language : ")
            developer_obj = Developer(emp_id, name, age, salary, language)
            print("\nDeveloper created successfully!")
        case 5:
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            print("4. Developer")
            show = int(input("\nEnter your choice: "))
            match show:
                case 1:
                    if person_obj is not None:
                        person_obj.display()
                    else:
                        print("\nPerson object not created.")
                case 2:
                    if employee_obj is not None:
                        employee_obj.display()
                    else:
                        print("\nEmployee object not created.")
                case 3:
                    if manager_obj is not None:
                        manager_obj.display()
                    else:
                        print("\nManager object not created.")
                case 4:
                    if developer_obj is not None:
                        developer_obj.display()
                    else:
                        print("\nDeveloper object not created.")
                case _:
                    print("\nInvalid Choice!")
        case 6:
            print("\nSubclass Details")
            print("Employee is subclass of Person: ", issubclass(Employee, Person))
            print("Manager is subclass of Employee: ", issubclass(Manager, Employee))
            print("Developer is subclass of Employee: ", issubclass(Developer, Employee))
        case 7:
            print("\nProgram Ended Successfully.")
            break
        case _:
            print("\nInvalid Choice! Please try again.")