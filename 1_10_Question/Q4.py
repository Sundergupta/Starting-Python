# Write a program to take user input of total working days & total present days and then count the percentage, if its below 75 , print not eligible for exam.
num1=int(input('Enter total working days '))
num2=int(input("Enter total present days "))
num3= num2/num1*100
print(num3)
if(num3>=75):
    print("you are eligible for exam.")
else:
    print("you are not eligible for exam.")