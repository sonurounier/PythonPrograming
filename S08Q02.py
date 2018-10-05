'''
Ask the user to enter a number.
- If the number is a single digit number, add 7 to it, 
     and print the number in its unit’s place
- If the number is a two digit number, raise the number to the power of 5, 
     and print the last 2 digits
- If the number is a three digit number, ask user to enter another number. 
     Add the 2 numbers and print the last 3 digits
'''
#Main Starts from here

num = input("Please enter 1 or 2 or 3 digit number":\n)

if num_length == 1:
    digit_1_num = int(num) + 7
    print("After operation on single digit number, new number is:",digit_1_num,"\n")
    digit_1_str = str(digit_1_num)
    print("Unit place digit number after operation is:",digit_1_str[-1],"\n")

elif num_length == 2:
    digit_2_num = int(num) ** 5
    print("After operation on double digit number, new number is:",digit_2_num,"\n")
    digit_2_str = str(digit_2_num)
    print("Last 2 digit number after operation is:",digit_2_str[-2:],"\n")

if num_length == 3:
    sec_3_digit =input("Please enter another number:\n")
    digit_3_num = int(num) + int(sec_3_digit)
    print("After operation on three digit number, new number is:",digit_3_num,"\n")
    digit_3_str = str(digit_3_num)
    print("Last 3 digit number after operation is:",digit_3_str[-3:],"\n")
