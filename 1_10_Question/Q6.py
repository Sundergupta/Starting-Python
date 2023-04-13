# Write a program to accept 2 number and operator(eg, +, -, *, / ) then perform calculation accordingly.
print("type 1 if you want to add")
print("type 2 if you want to sub")
print("type 3 if you want to muntiply")
print("type 4 if you want to Divide")
a =int(input(''))
if(a==1):
    num1=int(input("Enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    print(num1+num2)
elif(a==2):
    num1=int(input("Enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    print(num1-num2)
elif(a==3):
    num1=int(input("Enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    print(num1*num2)
elif(a==4):
    num1=int(input("Enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    print(num1/num2)