#Print Multiplication Table of 17

def Multiplication_Table(number):
    for i in range(1,11):
        print(number,"x",i,"=",number*i)

#Main Starts from here
Multiply_no=int(input("Please Enter the number for Multiplication table:"))
Multiplication_Table(Multiply_no)
