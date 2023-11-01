import encripter


#FUNCTION CALLING
quote=input("Which quote to you want to encript?\n>>")
if quote == "":
    quote = "nothing tbh"
diff = encripter.different(quote)
encripted, letter_sub  = encripter.encripting(quote)
encripter.writing_key(letter_sub)
print(f"\n{encripted}\n") #Tells the user what the encripted item is!