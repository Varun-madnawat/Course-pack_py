#1. Write a Python program to handle a Zero Division Error exception when dividing a number by zero.
# def divide_numbers(numerator, denominator):
#     try:
#         result = numerator / denominator
#         print("Result:", result)
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero. Please provide a non-zero denominator.")
# divide_numbers(5,0)

#2. Write a Python program that executes division and handles an Arithmetic Error exception if there is an arithmetic error.
# def divide_numbers():
#     try:
#         numerator = float(input("Enter the numerator: "))
#         denominator = float(input("Enter the denominator: "))
#         result = numerator / denominator
#         print("Result:", result)
#     except ValueError:
#         print("Error: Please enter valid numerical values.")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except ArithmeticError as e:
#         print(f"Error: ArithmeticError - {e}")

# divide_numbers()

#3. Write a Python program input, add two integers only and handle the exceptions.
# try:
#     num1 = int(input("Enter integer 1: "))
#     num2 = int(input("Enter integer 2: "))
#     print('result: ',num1+num2)
# except ValueError:
#     print('Error: Please enter valid integer values')

#4. Write a Python program that prompts the user to input an integer and raises a Value Error exception if the input is not a valid integer.
# def valid_integer():  
#     try:
#         user_input = input("Enter an integer: ")
#         num = int(user_input)
#         print("You entered:", num)
#     except ValueError:
#         print("Error: Please enter a valid integer.")
# valid_integer()

#5. Write a Python program that prompts the user to input a number and handles a Keyboard Interrupt exception if the user cancels the input.
# def get_user_input():
#     try:
#         user_input = input("Enter a number: ")
#         print("You entered:", user_input)
#     except KeyboardInterrupt:
#         print("\nUser cancelled the input.")
# get_user_input()