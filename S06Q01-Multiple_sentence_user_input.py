def vowel_a_check(string):
    #print(string)
    length=len(string)
    
    count=0
    value1=0
    while count<length:
        #print(string[count])
        if string[count]=="a":
            value1=1
            break
        count=count+1
        
    return int(value1)

'''
below codes take input and break till new line before enter key
'''
lines = []
while True:
    line = input()
    if line:
        lines.append(line)   #append the next line to previous line

    else:
        break
text = '\n'.join(lines)
#text = lines.append(line)
print(text)

#print("entered text")
#for x in range(len(lines)):
#    print(lines[x])


numwords=0
total_vowel_word=0

for i in lines:
    wordlist=i.split()
    #print("wordlist after split function",wordlist)
    #if wordlist == []:
     #   c_words+=1
     #for vowel_a in wordlist:
         
    numwords+=len(wordlist)
    #print("lenght of words",len(wordlist))
    #numwords=numwords+len(wordlist)
    #print("numwords value after split function", numwords)
    temp_vowel_count=0 #one line loop for vowel count check, as after next line value cannot be stored for count
    for j in range(len(wordlist)):
        vowel_count=vowel_a_check(wordlist[j])
        #print(word_vowel_count)
        #if word_vowel_count==1:
        temp_vowel_count=temp_vowel_count+vowel_count
        #print("word_vowel_count",word_vowel_count)
    total_vowel_word=total_vowel_word+temp_vowel_count
    #print("final_vowel",final_vowel)
print("number of word with vowel a:",total_vowel_word)
        

print("words:" ,numwords)


