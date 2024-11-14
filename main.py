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