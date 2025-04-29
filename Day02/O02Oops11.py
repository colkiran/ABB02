
class Employee:

    def __init__(self, name):
        self.__name = name          # private variable
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])

emp1 = Employee("Richard")

print(emp1)
print("-" * 60)

# access the private variable
# print(emp1.__name)
# print(emp1.__dict__)
print(emp1._Employee__name)
emp1._Employee__name = "Kennedy"

print("-" * 60)
print(emp1)
