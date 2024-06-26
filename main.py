
# * Nested class = A class defined within another class 
# *                class Outer:
# *                    class Inner:

# * Benefits: Allows you to logically group classes that are closely related
# *           Encapsulated private details that aren't relevant outside of the outer class 
# *           Kepps the namespace clean; reduces the possibilty of naming conflits 

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employees(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company("Krusty Krab")
company2 = Company("Chum Bucket")

print(company1.company_name)
print(company2.company_name)


company1.add_employees("Eugene", "Manager")
company1.add_employees("Spongebob", "Cook")
company1.add_employees("Squidward", "Cashier")

company2.add_employees("Sheldon", "Manager")
company2.add_employees("Karen", "Cashier")

print(company1.list_employees())

for employee in company1.list_employees():
    print(employee)


print(company2.list_employees())

for employee in company2.list_employees():
    print(employee)
    

# class Nonprofit:
#     class Employee:
#         print("this is the second class")