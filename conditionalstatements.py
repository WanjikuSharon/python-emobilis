#if...else...statement

votes = 100
if votes > 10000:
    print("You won")
else:
    print("You lost")

#GRADE CALC
marks = int(input("Your Math score"))
print(marks)

if marks > 80 and marks <=100:
    print("Your grade is: A")
elif marks > 70 and marks <=80:
    print("Your grade is: B")
elif marks > 60 and marks <=70:
    print("Your grade is: C")
elif marks > 50 and marks <=60:
    print("Your grade is: D")
elif marks > 40 and marks <=50:
    print("Your grade is: E")
elif marks > 20 and marks <=40:
    print("Your grade is: F")
elif marks > 0 and marks <=20:
    print("Your have failed")
else:
    print("Enter a number between 0 and 100")