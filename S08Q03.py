'''
Ask the user to enter a number.
- If the user enters a number as 5, then
generate the following string :
- 00001111222233334444- If the user enters the number as 3, then
generate the following string :
- 001122
'''

#Main Starts from here

num = input("Please enter a number more than 1:\n")

num_int = int(num)

for i  in range(num_int):
    print(str(i)*(num_int-1),end='')
