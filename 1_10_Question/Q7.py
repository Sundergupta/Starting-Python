# Write a program to calculate library charge according to - till 5 days Rs 2/day, 6 to 15 days Rs 4/day , 15 to 30 days Rs 7/day after 30 days Rs 10/day.
day =int(input("Enter your days"))
if(day<=5):
    print("your price is ",day*2)
elif(day>=6<=15):
    print("your price is ",day*4)
elif(day>15<=30):
    print("your price is ",day*7)
elif(day>30):
    print("your price is ",day*10)