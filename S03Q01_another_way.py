""" This program will check digit of a number
"""

# Implement the helper functions here

def perform_check(number):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    if number<10 or number>999:
        print ("Entered number is",number)
    elif number>=10 and number<=99:
        print ("Entered number",number, "is 2 digit")
    elif number>99 and number<1000:
        print("Entered number",number, "is 3 digit")
            

def get_number():
    x=input("Enter the number: ")
    return int(x)

# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)

