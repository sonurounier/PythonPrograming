def find_words(string, search):
    string_list = string.split()
    search_list = search.split()

    match = 0
    for text_word in string_list:
        for search_word in search_list:
            if search_word == text_word:
                match += 1
    if match == len(search_list):
        return True
    else:
        return False
    
def replace_word(string, search, replace):
    string_list = string.split()
    temp_word = []
    for i in string_list:
        if i !=search:
            temp_word.append(i)
        else:
            temp_word.append(replace)
    return temp_word
    

#Main Starts from here:

text = input("Enter a sentence:\n")
search_word = input("Enter the word to search in string:\n")
search_result = find_words(text, search_word)
replace_txt = input("Enter a word to replace in string:\n")

if search_result == True:
    print("Word found.:\n")
    modified_string = replace_word(text, search_word,replace_txt)
    print("Modified string:"," ".join(modified_string))

else:
    print("Word not found.")
