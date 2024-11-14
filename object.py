from main import Student
from main import Person

student1 = Student()
print(student1.first_name +" " + student1.last_name)

student2 = Student()
print(student2.first_name)

dad = Person("Harun Simwa", "Male", "Deceased", "Chief Magistrate")
mom = Person("Lydia Simwa", "Female", "Divorced", "Teacher")
bro = Person("Allan Ndungu", "Male", "Single", "Student")
print(dad.gender)
print(dad.marital_status)
print(mom.occupation)
print(bro.name)
print(f"Name: {dad.name}, Gender: {dad.gender}, Marital Status: {dad.marital_status}, Occupation: {dad.occupation}")




