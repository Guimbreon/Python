import random
import string
#COUNT THE AMOUNT OF DIFFERENT LETTERS
def different(quote):
    diff=""
    for thing in quote:
        if thing not in diff:
            diff+=thing
    return diff
#See all the diferent letters
def substitution(diff):
    letter_sub={}
    for letter in diff:
        letter_sub[letter]=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))

    return letter_sub
#Encripting
def encripting(quote):
    letter_sub = substitution(quote)
    quote_2=""
    for letter in quote:
        quote_2+=letter_sub[letter]
    first_part=""
    second_part=""
    i=0
    for letter in quote_2:
        if i%2==0:
            first_part+=letter
        else:
            second_part+=letter
        i+=1
    encripted=first_part+second_part
    return encripted, letter_sub
#Creates the key
def writing_key(letter_sub):
    with open(input("What file do u want to put the doc_keys?\n>>"), "w") as file:    
        for letter in letter_sub:
            file.write(f">{letter}\n{letter_sub[letter]}\n")
