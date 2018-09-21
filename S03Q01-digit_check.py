""" This program will check digit of a number
"""

# Implement the helper functions here

def perform_check(number):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    original_number=number
    digit_count=0
    while(numer>0):
        number=number//10
        digit_count=digit_count+1
        if digit_count==2:
            print("Entered number",original_number,"is",digit_count,"digit")
        elif digit_count==3:
            print("Entered number",original_number,"is",digit_count,"digit")
        else:
            print("Entered number is",original_number)
            

def get_number():
    x=input("Enter the number: ")
    return int(x)

# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)

