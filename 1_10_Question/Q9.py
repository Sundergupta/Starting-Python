# Write a program to accept number from 1 to 7 and display name of the day like 1 for Sunday, 2 for Monday and so on.
a = int(input("Enter number 1 - 7 to know what day it is "))
if(a==1):
    print("Monday")
elif(a==2):
    print("tuesday")
elif(a==3):
    print("Wednesday")
elif(a==4):
    print("Thursday")
elif(a==5):
    print("Friday")
elif(a==6):
    print("sutarday")
elif(a==7):
    print("sunday")
else:
    print("please type number between 1 - 7")