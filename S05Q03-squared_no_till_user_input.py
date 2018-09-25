"""
This progrm Print all the number which are perfect square from 1 till user input
"""

def perfect_square(num_to_check):
    i=1
    odd_sum=0
    while odd_sum<num_to_check:
        odd_sum=odd_sum+i
        if odd_sum==num_to_check:
            print(f"{num_to_check:5}")
        i=i+2

def square_check(num):
    print("Below numbers from 1 to", num, "is a perfect square number")
    for i in range(1, num+1):
        x=perfect_square(i)

#Main starts from here

number=int(input("Enter number to check all perfect square number from 1 till your input: "))
square_check(number)


