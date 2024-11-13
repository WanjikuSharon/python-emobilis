# create a function called greet that takes a persons name as an argument and returns
# a greeting message. if the name is 'Alice' or 'Bob' it returns a personalised
# greeting, for any other name it should return a general greeting
def greet(name):
    if name == "Alice" or name == "Bob":

        return f"{name} I hope you are doing well"

    else:
        return f"{name} Good morning"

#print(greet("Alice"))
# Get the user's name as input
user_name = input("Please enter your name: ")

# Call the function with the user input
print(greet(user_name))
# write a python program that finds a maximum of three numbers
def maximum(one, two, three):
    # Use the built-in max() function to find the largest number
    return max(one, two, three)

# Test the function with example inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the function and display the result
print(f"The maximum of the three numbers is: {maximum(num1, num2, num3)}")



# create a python function that sums all numbers in a list
def my_list(numbers):
    # Use the built-in sum function to sum all numbers in the list
    total = sum(numbers)
    return f"The sum of the numbers is {total}"

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7]

# Call the function and print the result
print(my_list(numbers))
