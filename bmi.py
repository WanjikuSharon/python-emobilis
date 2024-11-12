name = input("Whats your name? ")
print("Good morning " +name)

#BMI
print("Good to know you wanna stay healthy by keeping your BMI in Check")

age = input("Whats your age? ")
print("You are " +age, " Years")

weight =input("Whats your weight(in kgs)? ")
print("You weigh " +weight, " kgs")

height =input("Whats your height(in cm)? ")
print("You`re" + height, " cm tall")

#BMI CALCULATOR
bmi =  int(weight)/int(height)/int(height) *10000

print(bmi)