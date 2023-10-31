import decripter
import sys

#get everything from the file and transform it into a dictionary
letter_sub={}
letters=[]
subs=[]
try:
    if sys.argv[1]=="":
        print("a")
except:
    print("You have to put this script followed by the key-file!\n")
    quit()

encripted=input("What's the encripted message u want to translate?\n>>")



subs,letter_sub = decripter.info(encripted,sys.argv[1])
quote = decripter.translation(encripted,subs,letter_sub)
#The translated quote!
print(quote)