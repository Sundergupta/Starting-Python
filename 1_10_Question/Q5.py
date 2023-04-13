# write a program to get user input of price and print final price to pay after discount (if price > 10000 - 20% disc , if price > 7000 and <= 100000 - disc 15%, if price <= 7000 - 10% disc )
num1=int(input("Enter your price:::"))
if (num1>10000):
    num2 =num1/100*20
    print("Your price with 20% discount is:: ",num2-num1)
elif(num1>7000<=10000):
    num3 =num1/100*15
    print("Your price with 15% discount is:: ",num3-num1)
elif(num1<=7000):
    num4 = num1/100*10
    print("Your price with 10% discount is:: ",num4-num1)