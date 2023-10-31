import encripter


quote = input("Which quote to you want to encript?\n>>")
diff = encripter.different(quote)
letter_sub = encripter.substitution(diff)
encripted = encripter.encripting(quote)
encripter.writing_key(letter_sub)
print(f"\n{encripted}\n") #Tells the user what the encripted item is!