

print("")
print("CURRENCY CONVERTER")
print("")

DollarsParameter = float(input("enter any amount in dollars = """))
PoundsParameter = float(input("enter any amount in Pounds = """))
print("")
def convertDollarstoNaira (DollarsParameter):
    DollarsParameter = float(DollarsParameter)
    Naira = DollarsParameter *414.59 
    return Naira
Value = convertDollarstoNaira(DollarsParameter) 

def convertPoundstoNiara (PoundsParameter):
    PoundsParameter = float(PoundsParameter)
    Naira2 = PoundsParameter *539.51 
    return Naira2
Value2 = convertPoundstoNiara(PoundsParameter) 

print("The value of the given Dollars in Naira is:", Value)
print("The value of the given Pounds in Naira is:", Value2)

print("")