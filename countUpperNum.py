#Count the number of uppercase letters and whitespace characters

def countUpperNum(word):
    initialUpper=0
    initialWhite=0;

    for i in range(0, len(word)):
        if word[i].isupper():
            initialUpper += 1
        if word[i].isspace():
            initialWhite += 1

    print("There is/are {} upper-case letters".format(initialUpper))
    print("There is/are {} whitespace characters ".format(initialWhite))
    return;

#call function

#ask for an input
word=input("Input a word or a sentence ")
countUpperNum(word)

#output: Input a word or a sentence Hi! How are you DoIng?
#There is/are 4 upper-case letters
#There is/are 4 whitespace characters 
