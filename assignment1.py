# create an atm that awards discounts to users depending on their

# withdrawal amount and display the total amount inclusive of the discounts.

# Withdrawal above 10,000 award a discount of 15%, withdrawal above 5000 give

# a discount of 10% and lastly a withdrawal of above 2000 give a discount of

# 5%

Name = input("What's your name? ")
print("Hello " + Name)

# Get the withdrawal amount
Withdrawal_Amount = int(input("Enter Amount to Withdraw: "))
print("Withdrawing... " + str(Withdrawal_Amount))

# Initialize discount to 0 in case no discount applies
Discount = 0

if Withdrawal_Amount > 10000:
    Discount = 0.15 * Withdrawal_Amount
elif Withdrawal_Amount > 5000 and Withdrawal_Amount <= 10000:
    Discount = 0.1 * Withdrawal_Amount
elif Withdrawal_Amount > 2000 and Withdrawal_Amount <= 5000:
    Discount = 0.05 * Withdrawal_Amount
else:
    print("You have no discount on a withdrawal of " + str(Withdrawal_Amount))

# Calculate the total withdrawal after discount
Total_Withdrawal = Withdrawal_Amount - Discount
print("Total amount after discount: " + str(Total_Withdrawal))

