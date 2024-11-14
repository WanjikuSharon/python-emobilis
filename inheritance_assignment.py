"""
from main import BankAccount, Deposit, Withdrawal

#Bank Account
customerA = BankAccount("Jasmine Kawai", 25, 100000, "12345",100000)

print(customerA.display_account())

#Deposit
customerA2 = Deposit("Jasmine Kawai", 25, 100000, "12345",100000, 50000)
print(customerA2.account_balanceh())

#Withdrawal
CustomerA3 = Withdrawal("Jasmine Kawai", 25, 100000, "12345",150000, 25000)

print(CustomerA3.bankfees())
"""
#New improved Code
from main import BankAccount, Deposit, Withdrawal

# Initialize the customer account
customerA = Withdrawal("Jasmine Kawai", 25, "12345", 100000)

# Display initial account details
print(customerA.display_account())

# Deposit money
print(customerA.deposit(50000))  # Depositing KES 50,000

# Withdraw money
print(customerA.withdraw(25000))  # Withdrawing KES 25,000

# Apply bank fees
print(customerA.apply_bank_fees())

# Display final account details
print(customerA.display_account())

#DONE
