""" Perform required operation based on number of digits
"""

# Implement the helper functions here

def do_1digit_oper(num):
    oper_number=num+7
    print(str(oper_number)+str(num))

def do_2digit_oper(num):
    oper_number=num**5
    print(str(oper_number)+str(num))

def do_3digit_oper(num):
    new_number=int(input("Please Enter another number: "))
    oper_number=num+new_number
    print(str(oper_number)+str(num))

def perform_check(number):
    """ This function uses helper functions if 1digit or 2digit or 3digit
        to perform the required operations
    """
    original_number=number
    digit_count=0
    while(numer>0):
        number=number//10
        digit_count=digit_count+1
        if digit_count==1:
            do_1digit_oper(original_number)
        elif digit_count==2:
            do_2digit_oper(original_number)
        else:
            do_3digit_oper(original_number)
            

def get_number():
    x=input("Enter either 1 or 2 or digit number: ")
    return int(x)

# Main starts from here
num1 = get_number()
perform_check(num1)

