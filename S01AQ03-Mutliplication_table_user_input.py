<<<<<<< HEAD
""" 
This program prints multiplication based on user input
"""

def print_mtable():
    #This function print multiplication table based on user input
    Multiply_num=int(input("Please Enter the number for Multiplication table:"))
    for i in range(1,11):
        #print(Multiply_num,"x",i,"=",Multiply_num*i)
        print(Multiply_num,"{: >1}".format("x"),"{: >2}".format(i),"{: >2}".format("="),"{: >3}".format(Multiply_num*i))

# Main starts from here
print_mtable()
=======
""" 
This program prints multiplication based on user input
"""

def print_mtable():
    #This function print multiplication table based on user input
    Multiply_num=int(input("Please Enter the number for Multiplication table:"))
    for i in range(1,11):
        #print(Multiply_num,"x",i,"=",Multiply_num*i)
        print(Multiply_num,"{: >1}".format("x"),"{: >2}".format(i),"{: >2}".format("="),"{: >3}".format(Multiply_num*i))

# Main starts from here
print_mtable()
>>>>>>> 35981c62382cc5bc47088ac8f040e7790dd3550f
