
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return "Name is {} \nSalary is {}".format(self.name, self.salary)

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value

emp1 = Employee("Jack", 30000)
print(emp1)

print("-" * 60)
print([emp for emp in emp1])        # list comprehension

print("-" * 60)
print(len(emp1))

print("-" * 60)
x = emp1[4]
print(f"x :{x}")

print("-" * 60)
emp1[2] = 'JSP'
print([emp for emp in emp1])
