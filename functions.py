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
