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

class Vehicle:
    def __init__(self, make, model, year, color, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type

