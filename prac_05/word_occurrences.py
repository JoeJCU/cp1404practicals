
words_dict = {

}  #empty dict for each iterations



def main():
    user_string = input("Enter some strings: ").split() #input and splits all the words up in the user input
    print(f"Text: {user_string}")

    for word in user_string: # loop through all words in the user input
        if word in words_dict:
            words_dict[word] += 1 #adds that word to the dictionery

        if word not in words_dict:
            words_dict[word] = 1 #


    for word,word_count in words_dict.items():
        print(f"{word}, {word_count}")





main()

