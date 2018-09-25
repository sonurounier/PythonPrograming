'''
This program prints multiplaction table based on user input using both "for" & "while" loop
'''

def print_mtable_for():
    #This function print multiplication table based on user input
    multiply_num=int(input("Enter the number for multiplication table: "))
    for i in range(1,11):
        print(f"{multiply_num:3}x{i:2}={multiply_num*i}")



def print_mtable_while():
    #This function print multiplication table based on user input
    multiply_num=int(input("Enter the number for multiplication table: "))
    i=1
    while i<11:
        print(f"{multiply_num:3}x{i:2}={multiply_num*i}")
        i=i+1

#Main starts from here
print("Print multiplication table using FOR loop logic\n")
print_mtable_for()


print("Print multiplication table using WHILE loop logic\n")
print_mtable_while()
