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

class Vehicle:
    def __init__(self, make, model, year, color, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        pm = self.width + self.length + self.length + self.width
        print(f"The perimeter is {pm} m")

    def area(self):
        ar = self.width * self.length
        print(f"The area is {ar} metres square")

    def display_measurement(self):
        print(f"The length is {self.length} and Width is {self.width}")



