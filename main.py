class Student:
    first_name = "Sharon"
    last_name = "Wanjiku"
    gender = "Female"
    age = "22"


class Person:
    def __init__(self, name,gender,marital_status,occupation):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation

    def salutation(self):
        print(f"Good morning {self.name}, you are a {self.gender} and you are {self.marital_status}")

    def display_name(self):
        print(f"I am {self.name}")

#Assignment
class Vehicle:
    def __init__(self, make, model, year, color, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type

class Rectangle:
    """
    A class to represent a rectangle with methods to calculate perimeter,
    area, and display dimensions.
    """
    def __init__(self, length, width):
        """
        Initialize the rectangle with length and width.
        Ensures length and width are positive numbers.
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.length * self.width

    def display_measurement(self):
        """
        Display the length and width of the rectangle.
        """
        print(f"The length is {self.length} m and the width is {self.width} m")
#End of the above assignment

#Inheritance
class Employee:#parent class
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
#Custom Function
    def display(self):
        return f"I am {self.name} and I am {self.age} years old"

class Manager(Employee):#child
    def __init__(self, name,age,gender,salary,education_level):
        super().__init__(name,age,gender,salary)
        self.education_level = education_level

class Developer(Employee):
    def __init__(self, name, age, gender, salary, langauge):
        super().__init__(name,age,gender,salary)
        self.language = langauge

class SalaryEmployee(Employee):
    def __init__(self, name,age,gender,salary,weekly_salary):
        super().__init__(name,age,gender,salary)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary + self.salary

class HoursEmployee(Employee):
    def __init__(self, name,age,gender,salary,hours_worked,hourly_rate):
        super().__init__(name,age,gender,salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return (self.hours_worked * self.hourly_rate) + self.salary

class CommissionEmployee(SalaryEmployee):
    def __init__(self,name,age,gender,salary,weekly_salary,commission):
        super().__init__(name,age,gender,salary,weekly_salary)
        self.commission = commission

    #method inherited also from child
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission