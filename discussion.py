# Python allows for user input, with this users can give inputs to te program
# [Section] The input() nmethod allows the users to give inputs to the program


user_name = input("\nPlease enter your username: ")
print(f"Hello {user_name}! Welcome to the Python course")


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
# The output is the concatenation of num1 and num2. The reason for this is the input() method assign any value as strings
# Use typcasting to convert string into numer and proceed with the operation
print(f"The sum of the two numbers is {num1 + num2}")


# With the user input, users can give inputs for the program to be used to control the application using control structure
# [Section] Control Structure
'''
    this is the multiple comment in python
'''
'''
    - Control structures can be divided into selection and repetition structures
        - SELECTION STRUCTURES (decision based on conditions)
            - used to execute specific set of statements based on whether a certain condition is true or false
            - if statements commonly used selection structure
                - the if statement evaluates a certain condition and execute a block of code if the condition is true
                - if-else syntax...

                    if <condition>:
                        <block of code>
                    else:
                        <block of code>
        
        - REPETITION STRUCTURES (repeats code multiple times)
            - also known as loops, are used to repeat a block of code multiple times until a certain condition is met
            - two main types:
                - for loop
                    - used to iterate over a sequence of values
                - while loop
                    - used to repeat a block of code as long as a certain condition is true

'''

# [Section] If-else statements
# If-else statements are used to choose between two or more code blocks depending on the condition
# Declare a variable to use for the conditional statement


num3 = 75

if num3 >= 60:
     print("Congratulations! You passed the senior program")
else:
     print("Thank you. You are not qualified to the senior program.")

# Note that in Python, curly braces ({}) are not needed to distinguish the code blocks inside the if or else block. Hence, indentations are important as Python uses indentations to distinguish parts of code as needed.

test_number = int(input("Please enter a number: "))

if test_number > 0:
     print(f"{test_number} is a positive number.")
elif test_number == 0:
     print(f"{test_number} is zero.")
else:
     print(f"{test_number} is a negative number.")

# Note that 'elif' is the shorthand for 'else if' in other programming language.
