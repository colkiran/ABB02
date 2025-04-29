class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{}".format(self.value)

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)


a = Number(10)
b = Number(3)
c = Number(5)

print("Add:",  a + b + c)
print("Subtract:", a - b - c)
print("Multiply:", a * b * c)
print("Divide:", a / b / c)
