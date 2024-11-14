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
""""
This was my code had few errors only at applying withdrawal method
#Assignment on Bank Account
class BankAccount:
    def __init__(self, name,age,balance,account_number,account_balance):
        self.name = name
        self.age = age
        self.balance = balance
        self.account_number = account_number
        self.account_balance = account_balance

    def display_account(self):
        return f"{self.name} you have kes {self.account_balance} in your account"

class Deposit(BankAccount):
    def __init__(self,name,age,balance,account_number,account_balance,deposit_amount):
        super().__init__(name,age,balance,account_number,account_balance)
        self.deposit_amount = deposit_amount


    def account_balanceh(self):
        # updating account balance
        self.account_balance = self.deposit_amount + self.account_balance
        return f"{self.name} your new account balance is {self.account_balance}"

class Withdrawal(BankAccount):
    def __init__(self,name,age,balance,account_number,account_balance, amount_withdrawing):
        super().__init__(name, age, balance, account_number, account_balance)
        self.amount_withdrawing = amount_withdrawing



    def display_withdrawing_amount(self):
        return f"{self.name} you are withdrawing {self.amount_withdrawing}"

    def bankfees(self):
        remaining_balance = self.account_balance - self.amount_withdrawing
        fees = 0.05 * remaining_balance
        return fees
#Ends here and improved code is the next
"""
class BankAccount:
    def __init__(self, name, age, account_number, account_balance):
        """
        Initialize the bank account with customer details.
        """
        self.name = name
        self.age = age
        self.account_number = account_number
        self.account_balance = account_balance

    def display_account(self):
        """
        Display the account holder's details and current balance.
        """
        return f"{self.name}, you have KES {self.account_balance} in your account."

    def apply_bank_fees(self):
        """
        Apply a 5% bank fee on the current account balance.
        """
        fees = 0.05 * self.account_balance
        self.account_balance -= fees
        return f"Bank fees of KES {fees:.2f} applied. New balance is KES {self.account_balance:.2f}."

    def deposit(self, deposit_amount):
        """
        Deposit a specified amount to the account.
        """
        self.account_balance += deposit_amount
        return f"{self.name}, you deposited KES {deposit_amount}. New balance is KES {self.account_balance}."

    def withdraw(self, withdrawal_amount):
        """
        Withdraw a specified amount from the account, ensuring sufficient balance.
        """
        if withdrawal_amount > self.account_balance:
            return f"Insufficient funds! Your balance is KES {self.account_balance}."
        else:
            self.account_balance -= withdrawal_amount
            return f"{self.name}, you withdrew KES {withdrawal_amount}. New balance is KES {self.account_balance}."


class Deposit(BankAccount):
    pass  # Inherits all methods from BankAccount


class Withdrawal(BankAccount):
    pass  # Inherits all methods from BankAccount

#This improved code applies to a single person for each method