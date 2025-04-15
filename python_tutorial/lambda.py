"""add = lambda x,y: x + y
minus = lambda x,y: x - y
multi = lambda x,y: x * y
divi = lambda x,y: x / y
power = lambda x,y: x**y
square = lambda x: x ** 3

x = int(input("Num1: "))
y = int(input("Num2: "))

print(" ")
print("\n Addition: ", add(x,y))
print("\n Subtraction: ", minus(x,y))
print("\n Multiplication: ", multi(x,y))
print("\n Division: ", divi(x,y))
print("\n Power: ", power(x,y))
print("\n Square: ", square(x))"""

x = int(input("Type a number: "))
square = lambda x: x * 3

print(square(x))