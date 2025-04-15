"""age = 12

while age < 18 :
    print("Still Young : " + str(age))
    age = age + 1 """
    
"""age = 12

while age < 18:
    print("Still Young: " + str(age))
    age = age + 1
else:
    print("Legal Age : " + str(age))"""
    

"""studentID = [2023,400,172,4340, 4345]
i = 0

while i < 3:
    print(studentID[i])
    i = i + 1
else:
    print("this is the last student " + str(studentID[4]))"""


""""
number = 1
while number <= 6:
    print("Hello World")
    number = number + 1 """

numbers = [1,2,3,4,5,6,7,8,9,10]

i = 0

while i < len(numbers):
    if(numbers[i] % 2 == 0):
        print("Even Number : " + str(numbers[i]))
        print("\n")
    else:
        print("Odd Numbers : " + str(numbers[i]))
    i = i + 1
    
    
    
print("\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Sample numbers
i = 0  

evens = []  # List for even numbers
odds = []   # List for odd numbers

while i < len(numbers):
    if numbers[i] % 2 == 0:
        evens.append(numbers[i])  # Store even numbers
    else:
        odds.append(numbers[i])   # Store odd numbers
    i += 1  

# ✅ Print combined odd and even numbers
print("Even Numbers: " + str(evens))
print("Odd Numbers: " + str(odds))
