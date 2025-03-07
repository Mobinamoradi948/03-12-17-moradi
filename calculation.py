# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Display results
print("\nResults:")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)

