# Write a program to check whether a person is eligible for vote or not if yes then capture gender too.
age= int(input("Enter your age"))
if (age>=18 and age<=60):
    print("you are good to go (you can vote)")
    Gender=input("Enter yor Gender")
else:
    print("you can not vote")