# num1 = 5 
# num2 = 6 
# num3 = 7 
#To take inputs from user 
num1 = float(input("Enter first side of triangle: "))
num2 = float(input("Enter second side of triangle: "))
num3 = float(input("Enter third side of triangle: "))
s = (num1+num2+num3)/2
area = (s*(s-num1)*(s-num2)*(s-num3)) ** 0.5
print ("area of triangle is %0.2f" %area)