import math
def main():
    digits = int(input("Enter the number of Pi Digits :"))
    PiNumber(digits)
    Close = input("If you want to exit program \nPlease type 'Close' :")
    exit(Close)
def PiNumber(digits):
    number = round(math.pi, digits)
    #len doesnt count anything pass . so we have to remove the decimal point for the length check
    number_str = str(number).replace('3.', '')
    #checking the length of number
    if len(number_str) <= 10:
        print("Pi Number you requested : ", number)
    else:
        print("Pi Digit you requested is too much: ")
    return number  #Pi
def exit(Close):
    while Close != "Close":
        print("Running Calculator again")
        digits = int(input("Enter the number of Pi Digits :"))
        PiNumber(digits)
        Close = input("If you want to exit program \nPlease type 'Close' :")
    return

main()
