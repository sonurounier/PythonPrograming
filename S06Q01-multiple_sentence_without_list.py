
def vowel_a_check(string):
    #print(string)
    length=len(string)
    
    count=0
    value=0
    while count<length:
        #print(string[count])
        if string[count]=="a":
            value=1
            break
        count=count+1
        
    return int(value)


#Main Starts from here
word_count = 0
total_a_vowel_word = 0

while True:
    character = str(input("Please enter sentence or press Enter to exit: \n"))
    if character == '':
        break
    word_list = character.split()
    
    print(word_list)
    print("length of words",len(word_list))
    word_count += len(word_list)
    vowel_count = 0
    for i in range(len(word_list)):
        vowel_count = vowel_count + vowel_a_check(word_list[i])
         
    total_a_vowel_word = total_a_vowel_word + vowel_count
            

print("total words", word_count)
print("total words with Vowel 'a'", total_a_vowel_word)
