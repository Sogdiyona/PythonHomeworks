def convert_cel_to_far(C):
    F=C * 9 / 5 + 32
    return F
C=float(input("Enter the a temperature in degrees Celsius: "))
print(C,"degrees C =",convert_cel_to_far(C),"degrees F")
def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    return C
F=float(input("Enter the a temperature in degrees Fahrenheit: "))
print(F,"degrees F =",convert_cel_to_far(F),"degrees C")