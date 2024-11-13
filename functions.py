def my_function():
    print("Hello Sharon")

#calling
my_function()

def my_family(name):
    print(name + " Simwa")

#calling
my_family("Sharon")
my_family("Allan")
my_family("Jasmine")

#Arbitrary Arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Ass: Function that takes 2 numbers as arguments and performs the summation and display the summation

def my_summation(one, two):
    # Ensure the arguments are treated as numbers
    result = int(one) + int(two)
    return result
    #print(f"The sum is {result}")

# Call the function with valid arguments
print(my_summation(8, 9))

def promote(name, age):
    if age > 18 and age < 23:
        return f"{name} you are {age} and you are promoted to University"

    elif age >= 24:
        return f"{name} you are {age} and you are promoted to work environment"
    else:
        return f"{name} you are {age} and you are supposed to be in highschool"


print(promote("Sharon", 16))