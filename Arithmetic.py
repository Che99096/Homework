import math

print()

number = int(input("ENTER AN INTEGER :"))
print("")

Exponent = int(input("Enter any exponent  = """))
square = math.pow(number,2)
squareroot = math.sqrt(number)
cuberoot = math.pow(number,1/3)
powerofnumber = math.pow(number,Exponent)
numberdivitself = number/number

print("")

print("The square of given number is: ",square)
print("The square root of given number is: ",squareroot)
print("The cuberoot of given number is: ",cuberoot)
print("The given number to the given exponent is: ",powerofnumber)
print("The given number divided by itself is: ",numberdivitself)

print("")
