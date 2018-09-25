'''
This program takes user input till he enters 0, and will find the max or min value
of entered number and find count of 1 or 2 or 3 digit entered number
'''


#Main Starts from here

min_num=0
max_num=0
one_digit_counter=0
two_digit_counter=0
three_digit_counter=0

while True:
    number=int(input("Please Enter any number or 0 to exit:"))
    if number==0:
        break
    if (min_num ==0) or (number<min_num):
        min_num=number
    if (max_num ==0) or (number>max_num):
        max_num=number
    
    if number<10:
        one_digit_counter=one_digit_counter+1
    elif number>=10 and number<=99:
        two_digit_counter=two_digit_counter+1
    elif number>99 and number<1000:
        three_digit_counter=three_digit_counter+1
print("Maximum of Entered number is", max_num)
print("Minimum of Entered number is", min_num)

print("Total 1 digit of Entered number is", one_digit_counter)
print("Total 2 digit of Entered number is", two_digit_counter)
print("Total 3 digit of Entered number is", three_digit_counter)

    
