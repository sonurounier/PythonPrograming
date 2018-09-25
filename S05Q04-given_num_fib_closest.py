"""
This program checks whether given number is fibonacci,
if not then find the closest fibonacci number
"""
def fibonacci_number():

    first_num, second_num = 1, 1
    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num
        

#Main starts from here

fib_check = int(input("Please Enter a number: "))
for fib_seq in fibonacci_number():
    #print("fib_seq")
    if fib_check == fib_seq:
        print("Entered number is a fibonacci number")
        break
    elif fib_seq<fib_check:
        prev_fib_number = fib_seq
        #print("previous number",prev_fib_number)

    if fib_seq>fib_check:
        print("Entered number is not a fibonacci number")
        fib1 = fib_seq - fib_check
        fib2 = fib_check - prev_fib_number
        #print("fib1: ",fib1, "fib2: ", fib2)

        if fib1 == fib2:
            print("Neares Fibonacci number of", fib_check, "is", fib_seq, "or", prev_fib_number)
        elif fib1<fib2:
            print("Neares Fibonacci number of", fib_check, "is", fib_seq)
        else:
            print("Neares Fibonacci number of", fib_check, "is", prev_fib_number)
        break
            

