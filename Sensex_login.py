import random

login_attempt = 1
#from termcolor import colored
number = random.randint(1, 25)
print(number)

while login_attempt < 5:
    #print("Enter Passcode:")
    guess = int(input("Enter Passcode:"))
    guess = int(guess)
    login_attempt = login_attempt + 1
    if guess < number-2:
        print("invalid passcode")
    if guess > number+2:
        print("INVALID PASSCODE")
    if (number+2)>= guess >= (number-2) and guess != number:
        print("InVaLiD PaSsCoDe")

        while login_attempt < 6:
            guess = int(input("Enter Passcode:"))
            guess = int(guess)
            login_attempt = login_attempt + 1
            if guess < number-2:
                print("invalid passcode")
            if guess > number+2:
                print("INVALID PASSCODE")
            if (number+2)>= guess >= (number-2) and guess != number:
                print("InVaLiD PaSsCoDe")
            if guess == number:
                print("Welcome !!!")
                break
        else:
            print("Login Failed !!!")
        break
    
    if guess == number:
        print("Welcome !!!")

        break
else:
    print("Login Failed !!!")
'''
while login_attempt < 6:
    guess = int(input("Enter Passcode:"))
    guess = int(guess)
    login_attempt = login_attempt + 1
    if guess < number-2:
        print("invalid passcode") # There are eight spaces in front of print.
    if guess > number+2:
        print("INVALID PASSCODE")
    #if guess <= number+2 or guess>= number-2:
    if (number+2) >= guess >= (number-2):
        print("InVaLiD PaSsCoDe")
    if guess == number:
        print("Welcome")
        break
'''
