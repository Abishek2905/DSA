# Print age and name
name = "Abi"
age = 28
print(f" My name is {name} and I am {age} years old.")

# Design a calculator
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
sum = number_1 + number_2
difference = number_1 - number_2
product = number_1 * number_2
division = number_1 / number_2
print(f"\nSum: {sum}")
print(f"\nDifference: {difference}")
print(f"\nProduct: {product}")
print(f"\nDivision: {division}")

# Check if a number is even or odd
number = int(input("\n Enter a number: "))
print (f"\nEven" if number % 2 == 0 else f"\nOdd")
print("\n")
# Print no from 1 to 10 in a loop
for i in range(1, 11):
    print(i)

# Write a function to greet someone
def greet(name):
    print(f"\nHello, {name}!")

greet("Abi")