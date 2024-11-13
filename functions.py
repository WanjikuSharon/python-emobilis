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
    print(f"The sum is {result}")

# Call the function with valid arguments
my_summation(8, 9)
