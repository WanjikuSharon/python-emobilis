from main import Employee, Manager, Developer, SalaryEmployee, HoursEmployee, CommissionEmployee

#parent class object implementation
accountant = Employee("Sharon Wanjiku", 22, "Female", "30,000")
security = Employee("Erastus Mwangi", 34, "Male", 50000 )

#child object
sot = Manager("Jasmine Wanjiku", 20, "Female", 40000, "Masters")
sob = Manager("Xanthe Wanjiku", 24,"Female", 10000000,"Doctorate")

#inheriting the method
print(sob.display())

#child object for Developer
web_dev = Developer("Aurora Rora", 28, "Female", 40000, "Python")
mobile_dev = Developer("Jin Shine", 21,"Male", 10000000, "Dart")

#inheriting the method
print(web_dev.display())

#salary employee
accountant1 = SalaryEmployee("Lydia Simwa", 32, "Female", 100000, 30000)

#method
print(accountant1.calculate_payroll())

#HourlyEmployee
accountant2 = HoursEmployee("Harun Simwa", "45", "Male", 100000000, 45, 4000)

#methods
print(accountant2.calculate_payroll())

#Commisioned employee
accountant3 = CommissionEmployee("Blessings Mel", 34,"Female", 500000, 100000, 40000)

#method
print(accountant3.calculate_payroll())


