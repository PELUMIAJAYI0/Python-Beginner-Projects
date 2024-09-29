def replace_word():
    
    str="Hi guy, i am pelumi"
    word_to_replace = input("Input the word to replace---> ")
    word_replacement = input("Input the word replacement---> ")
    
    str = str.replace(word_to_replace, word_replacement)
    
    #helps to replace another owrd in a string
    print(str)
    #print(str.replace(word_to_replace, word_replacement))


while True:
    replace_word()
    cont = input("Do you want to continue? (yes/no)---> ")
    if cont.lower() == "no":
        break