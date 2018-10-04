'''
Prompt the user to enter a long sentence
        - What is the last character in the sentence ?
        - What are the last 5 characters in the sentence ?
        - Print the characters that are present in 2nd and 5th position of the sentence
        - Print the character at the center of the string, along with the 2 adjoining characters. 
        Ex : If the string entered is "Web Browser”
        the character at its centre is "r" and so print "Bro"
'''

def get_middle_char(str):
    length = len(str)
    return int((length // 2) + (length % 2) - 1)


#Main starts from here

sentence = input("Enter a long sentence:\n")
middle=get_middle_char(sentence)
print(middle)
print("\nLast character of sentence is: ",sentence[-1])

print("\nLast 5 character of sentence are: ",sentence[-5:])

print("\n2nd & 5th character of sentence are: ",sentence[1],sentence[4] )

print("\nMiddle plus adjoining character of sentence are: ",sentence[middle-1:middle+2])
