'''
You invite home 10 of your closest friends and play a simple game of luck.
Each of your friend picks up a card from a stack of cards numbered from 300 to 325. 
The person with the highest number winsSimulate this simple game using Python
[ Hint : Make sure that no 2 friends get the same numbered card ]
'''

from random import sample
 
def max_num(list_max):
    #print(list_max)
    maximum=0
    for i in list_max:
        #print("i",i)
        if i>maximum:
            maximum=i
    return maximum

def main():
    friends_num= 10
    cards = sample(range(300,326),friends_num)
    print (cards)
    max_card= max_num(cards)
    print ("Highest card winner: ",max_card)
 
main()
