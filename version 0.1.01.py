import math
def PiNumber(digits):
    number = round(math.pi, digits)
    #len doesnt count anything pass . so we have to remove the decimal point for the length check
    number_str = str(number).replace('3.', '')
    #checking the length of number
    if len(number_str) <= 10:
        print("Pi Number you requested : ", number)
    else:
        print("Pi Digit you requested is too much: ")
    return number

digits =int(input("Enter the number of Pi Digits :"))
PiNumber(digits)