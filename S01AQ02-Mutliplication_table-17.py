""" 
This program prints multiplication of 17
"""

def print_mtable(num):
    #This function print multiplication table based on user input
    for i in range(1,11):
    #print(Multiply_num,"x",i,"=",Multiply_num*i)
        print(num,"{: >1}".format("x"),"{: >2}".format(i),"{: >2}".format("="),"{: >3}".format(num*i))

# Main starts from here
multiply_num=17
print_mtable(multiply_num)
