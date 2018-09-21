""" What does this program do ?
"""

def do_action(mark, first_class, second_class, fail):
    if mark>=first_class:
        print("Congrats!!! You Scored 1st Class")
    
    elif mark>=second_class and mark<first_class:
        print("Congrats!!! You Scored 2nd Class")

    elif mark<second_class and mark>fail:
        print("Congrats!!! You Passed")

    else:
        print("Sorry... You Fail")

def get_students_mark():
    English=int(input("Please Enter marks obtained in English: "))
    Science=int(input("Please Enter marks obtained in Science: "))
    Maths=int(input("Please Enter marks obtained in Maths: "))
    avg=(English+Science+Maths)/3
    return int(avg)

def do_percentage(num1, num2):
              num=(num1/num2)*100
              print("Your Percentage: ",'{0:.2f}%'.format(num))

# Main starts from here
English_full = 80
Science_full = 90
Maths_full = 100
Average_full=int((English_full+Science_full+Maths_full)/3)
first_class_cutoff = int(90/100*Average_full)
secondt_class_cutoff = int(75/100*Average_full)
fail_cutoff = int(35/100*Average_full)
Avg_Mark = get_students_mark()
do_percentage(Avg_Mark, Average_full)
do_action(Avg_Mark, first_class_cutoff, secondt_class_cutoff,fail_cutoff)
