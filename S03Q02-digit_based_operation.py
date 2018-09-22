""" Perform required operation based on number of digits
"""

# Implement the helper functions here

def reminder(num):
    if num<10:
        return (num)
    elif num>=10:
        num_rem=num%10
        return (num_rem)

def do_1digit_oper(num):
    oper_number=num+7
    print("After adding 7 to 1 digit number, result is: ",oper_number)
    unit_number=reminder(oper_number)
    print("Unit place number is ",unit_number)

def do_2digit_oper(num):
    oper_number=num**5
    print("10 power 5 is",oper_number)
    unit_number=reminder(oper_number)
    print("Unit place number is ",unit_number)

def do_3digit_oper(num):
    new_number=int(input("Please Enter another number: "))
    oper_number=num+new_number
    print("After adding new number to previous 3 digit number, result is: ",oper_number)
    unit_number=reminder(oper_number)
    print("Unit place number is ",unit_number)

def perform_check(number):
    """ This function uses helper functions if 1digit or 2digit or 3digit
        to perform the required operations
    """
    if number<10:
        do_1digit_oper(number)
    elif number>=10 and number<=99:
        do_2digit_oper(number)
    elif number>99 and number<1000:
        do_3digit_oper(number)
            

def get_number():
    x=input("Enter either 1 or 2 or 3 digit number: ")
    return int(x)

# Main starts from here
num1 = get_number()
perform_check(num1)

