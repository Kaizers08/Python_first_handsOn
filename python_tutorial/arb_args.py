"""def allnames(*names):
    for name in names:

        print("Hello,", name)

allnames("Jaireell", "Son", "Santos", "Regala")"""

"""def sayHello(firstName, lastName):
    print(firstName + " " + lastName)
sayHello(lastName="Solutions", firstName="SDPT")"""

def summationOf(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(summationOf(1,2,3,4,5,6,7,8,9,10))