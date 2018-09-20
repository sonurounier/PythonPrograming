""" 
Mention a statement about what this program does.
"""

def get_username():
     
    user_name=str(input("Please Enter your name: "))
    return user_name
    
    # Your solution code should go in here

def say_hello(user):
    print("Hello", user, "!!!")

def main():
    name = get_username()
    say_hello(name)
    
# Main starts from below
main()
